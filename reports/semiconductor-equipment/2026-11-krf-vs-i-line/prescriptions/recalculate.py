"""Reproduce the ZEISS common-aperture geometry and the axial i-line NA. Standard library only."""
import csv
import math
from statistics import median
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
GLASS = {"FK5", "LF5", "LLF1", "SUPRA1", "SILUV"}


@dataclass
class Surface:
    number: int
    radius: float
    distance: float
    medium: str
    index: float
    aperture: float
    coefficients: tuple = ()

    def sag(self, height):
        curvature = 1 / self.radius if self.radius else 0
        root = math.sqrt(1 - (curvature * height) ** 2)
        sphere = curvature * height**2 / (1 + root)
        return sphere + sum(a * height**(4 + 2*j) for j, a in enumerate(self.coefficients))

    def slope(self, height):
        curvature = 1 / self.radius if self.radius else 0
        sphere = curvature * height / math.sqrt(1 - (curvature * height)**2)
        return sphere + sum((4 + 2*j)*a*height**(3 + 2*j)
                            for j, a in enumerate(self.coefficients))


def read_tsv(name):
    with (HERE / name).open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def read_surfaces(design):
    surfaces = [
        Surface(int(row["surface"]), float(row["radius_mm"]), float(row["thickness_mm"]),
                row["medium_after"], float(row["index_after"]), (0.0 if row["semidiameter_mm"] == "NA" else float(row["semidiameter_mm"])))
        for row in read_tsv(design + "-surfaces.tsv")
    ]
    if design == "krf":
        for row in read_tsv("krf-aspheres.tsv"):
            assert float(row["K"]) == 0, "These data use a spherical base conic"
            surfaces[int(row["surface"])].coefficients = tuple(float(row[f"C{i}"]) for i in range(1, 7))
    return surfaces


def print_geometry(surfaces):
    print("front/back  material        D       CT       ET     D/CT     D/ET")
    powered = []
    plates = 0
    counts = [0, 0, 0]  # spherical / aspheric / plane (all glass faces)
    for front, back in zip(surfaces, surfaces[1:]):
        if front.medium not in GLASS:
            continue
        height = min(front.aperture, back.aperture)
        diameter = 2 * height
        edge = front.distance + back.sag(height) - front.sag(height)
        for face in (front, back):
            counts[1 if face.coefficients else (0 if face.radius else 2)] += 1
        if front.radius or back.radius or front.coefficients or back.coefficients:
            powered.append((diameter, front.distance, edge, diameter/front.distance, diameter/edge))
        else:
            plates += 1
        print(f"S{front.number:02}/S{back.number:02} {front.medium:>8} {diameter:8.3f} "
              f"{front.distance:8.3f} {edge:8.3f} {diameter/front.distance:8.2f} {diameter/edge:8.2f}")

    print(f"Powered lenses: {len(powered)}; plane plates: {plates}; "
          f"spherical/aspheric/plane surfaces: {counts}")
    for label, values in zip(("D", "CT", "ET", "D/CT", "D/ET"), zip(*powered)):
        print(f"{label} min / median / max: {min(values):.6f} / {median(values):.6f} / {max(values):.6f}")
    for f in surfaces:
        if f.coefficients:
            delta = sum(a*f.aperture**(4 + 2*j) for j, a in enumerate(f.coefficients))
            print(f"S{f.number} departure at its clear edge: {delta:+.6f} mm; "
                  f"slope angle: {math.degrees(math.atan(f.slope(f.aperture))):+.3f} deg")


def axial_clearance(surfaces, vertices, na):
    """Worst ratio of axial ray height to clear semidiameter, tracing from the image."""
    z, height = vertices[-1], 0.0
    vz, vy = -math.sqrt(1 - na**2), na
    worst = (0.0, 0)
    for i in range(len(surfaces)-2, 0, -1):
        surface = surfaces[i]
        travel = (vertices[i] - z) / vz
        for _ in range(30):
            y = height + travel*vy
            slope = surface.slope(y)
            step = (z + travel*vz - vertices[i] - surface.sag(y)) / (vz - slope*vy)
            travel -= step
            if abs(step) < 1e-10:
                break
        else:
            raise ArithmeticError(f"Intersection did not converge at S{i}")
        z += travel*vz
        height += travel*vy
        worst = max(worst, (abs(height) / surface.aperture, i))
        norm_z = 1 / math.hypot(1, slope)
        norm_y = -slope * norm_z
        cos_in = -(vz*norm_z + vy*norm_y)
        eta = surface.index / surfaces[i-1].index
        normal_component = eta*cos_in - math.sqrt(1 - eta**2*(1 - cos_in**2))
        vz, vy = eta*vz + normal_component*norm_z, eta*vy + normal_component*norm_y
    return worst


def print_iline_na(surfaces):
    vertices = [0.0]
    for surface in surfaces[:-1]:
        vertices.append(vertices[-1] + surface.distance)
    lower, upper = 0.60, 0.66
    assert axial_clearance(surfaces, vertices, lower)[0] < 1 < axial_clearance(surfaces, vertices, upper)[0]
    for _ in range(40):
        mid = (lower + upper)/2
        if axial_clearance(surfaces, vertices, mid)[0] <= 1:
            lower = mid
        else:
            upper = mid
    _, stop = axial_clearance(surfaces, vertices, lower)
    print(f"Axial clear-aperture limit: NA={lower:.6f}, S{stop}")


if __name__ == "__main__":
    for design in ("iline", "krf"):
        optics = read_surfaces(design)
        print(design)
        print_geometry(optics)
        if design == "iline":
            print_iline_na(optics)
