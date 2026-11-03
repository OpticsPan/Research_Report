"""Compute plane-parallel and spherical element geometry from ZEISS US6522484B1, Table 5.

H_max is published on only one face of eight lenses. The two-face thickness at
that height is a conditional evaluation of the printed radii, not a measured edge.
The 341 mm figure for lens 529 is a lens diameter stated separately in the text.
"""
import csv
import math
from pathlib import Path
from statistics import median

DATA = Path(__file__).with_name("krf-figure5.tsv")


def sag(radius, height):
    """Signed spherical sag in mm, zero for a plane."""
    u = height / radius
    return height * u / (1 + math.sqrt(1 - u * u))


def elements():
    with DATA.open(encoding="utf8") as source:
        for row in csv.DictReader(source, delimiter="\t"):
            ct = float(row["ct_mm"])
            front = float(row["r_front_mm"])
            rear = float(row["r_rear_mm"])
            diameter = thickness_at_h = None
            if row["h_max_mm"] != "NA":
                h = float(row["h_max_mm"])
                diameter = 2 * h
                thickness_at_h = ct + sag(rear, h) - sag(front, h)
            elif row["diameter_in_text_mm"] != "NA":
                diameter = float(row["diameter_in_text_mm"])
            yield row, diameter, thickness_at_h


if __name__ == "__main__":
    records = list(elements())
    powered = [row for row, _, _ in records if row["element"] != "P5"]
    ct = [float(row["ct_mm"]) for row in powered]
    radii = [abs(float(row[key])) for row in powered for key in ("r_front_mm", "r_rear_mm")]
    print(f"{len(powered)} lenses plus P5; CT min/median/max {min(ct):.3f}/{median(ct):.3f}/{max(ct):.3f} mm")
    print(f"Absolute radius range {min(radii):.3f} to {max(radii):.3f} mm")
    print("Lens  diameter basis   D(mm)   D/CT   t(H)*mm   D/t(H)*")
    for row, d, t in records:
        if d is None:
            continue
        basis = row["h_side"] if row["h_side"] != "NA" else "text"
        conditional = f"{t:7.3f} {d/t:9.2f}" if t is not None else "      -         -"
        print(f"{row['element']:>4} {basis:>15} {d:7.1f} {d/float(row['ct_mm']):6.2f} {conditional}")
