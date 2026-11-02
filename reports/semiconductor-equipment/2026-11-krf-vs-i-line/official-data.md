# 官方数据底稿 · i-line 与 KrF

本页将产品规格和项目档案整理为可引用的 Markdown。数值沿用来源中的上限、下限及典型值。来源编号对应[报告来源表](sources.md)。

## 两款 Nikon SF 步进机

| 原厂规格 | SF100（i-line） | SF200（KrF） |
| --- | ---: | ---: |
| 光源波长 | 365 nm | 248 nm |
| 最大 NA | 0.52 | 0.63 |
| 缩小倍率 | 1/4 | 1/4 |
| 曝光场 | 25 × 33 mm | 26 × 33 mm |
| 标称分辨率 | ≤400 nm | ≤150 nm |
| 套刻规格 | ≤45 nm | ≤28 nm |
| 200 mm 晶圆产能 | ≥120 片/小时 | ≥120 片/小时 |
| 300 mm 晶圆产能 | ≥80 片/小时 | ≥110 片/小时 |

两台都是步进机。线宽规格上限差为 (400−150)/400 = 62.5%，NA、幅面和产品代际也有变化。套刻按日文原厂规格的「重ね合わせ精度」登记，网站未在该表给出统计公式。两个晶圆直径分别比较；每片曝光场数和剂量缺失，表中下限不等于同配方的实测产能。[S30 · SF100](https://www.jp.nikon.com/business/products-and-services/semiconductor-lithography/systems/i-line-steppers/lineup/product-specification.nsr-sf100/) · [S31 · SF200](https://www.jp.nikon.com/business/products-and-services/semiconductor-lithography/systems/krf-steppers/lineup/product-specification.nsr-sf200/)

## 欧委会登记的项目

| 项目 | 周期 | 范围与成果 | 总成本 / 欧方出资 |
| --- | --- | --- | --- |
| 2048，ASM Lithography 牵头 | 1988-11-01 至 1991-10-31，36 个月 | 248 nm 曝光样机，同时涉及材料和环境集成 | 均未列值 |
| 5002，Carl Zeiss 牵头 | 1990-01-01 至 1992-12-31，36 个月 | DUV 物镜项目。档案记录原型演示 0.25 µm 结构；另研究直径可达 250 mm 镜片的装夹稳定性 | 均未列值 |
| 1805 / ASPRO，ASM Lithography 牵头 | 1992-05-27 至 1994-11-26，30 个月 | 改进生产用 i-line 步进机，目标 0.4 µm。成果记录点名 PAS 5500/100、可变 NA 与可变照明相干性 | 均未列值 |
| 27115 / SASSOL 2，STMicroelectronics 牵头 | 1998-01-01 至 1999-06-30，18 个月 | 亚四分之一微米扫描项目；档案未指明设备型号、波长或 ASML/Nikon 经费份额 | 1,020 万 / 510 万欧元 |

ASPRO 与 2048 的合同期相差 6 个月，交付阶段、验证对象和参与者有别。5002 与 2048 的日期有交叠，不宜合计为一条串行研发周期。SASSOL 2 的欧方出资占总额 50%，已经包含在总成本中。[S08 · 2048](https://cordis.europa.eu/project/id/2048) · [S32 · 1805](https://cordis.europa.eu/project/id/1805) · [S33 · 5002](https://cordis.europa.eu/project/id/5002) · [S36 · 27115](https://cordis.europa.eu/project/id/27115)

## Gigaphoton KrF 光源

| 原厂典型值 | G10K | G20K |
| --- | ---: | ---: |
| 波长 | 248 nm | 248 nm |
| 单脉冲能量 | 10 mJ | 10 mJ |
| 重复频率 | 1,000 Hz | 2,000 Hz |
| 平均输出光功率 | 10 W | 20 W |
| 半高全宽 FWHM | 0.6 pm | 0.6 pm |
| E95 带宽 | 2.0 pm | 2.0 pm |
| 剂量稳定度 | 0.5% | 0.4% |

以单脉冲能量乘重复频率，分别为 0.010 J × 1,000/s = 10 W、0.010 J × 2,000/s = 20 W。按连续脉冲串计算，相邻脉冲间隔从 1.0 ms 缩短到 0.5 ms。整机还须搬片、步进、对焦和测量，产能不能按光功率等比换算。[S17 · G10K](https://www.gigaphoton.com/products/8027) · [S37 · G20K](https://www.gigaphoton.com/products/8032)
