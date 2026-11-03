# 仓库变更记录

本日志收录报告首次发布、影响关键数字或结论的修订，以及目录、模板和协作流程的调整。错字和排版调整可通过 Git 历史查询。

把新条目连同对应变更一次提交到 `main`，并将条目写在最上方，按日期（YYYY-MM-DD）归档。每条写明改了什么、对读者或作者有什么影响，并链接对应的报告、Issue 或提交。报告勘误还应在正文修订记录中保留原值、新值和修订依据。

## 2026-11-03

- [ASML 报告](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)以 ZEISS 0.65 NA i-line 和 0.80 NA KrF 专利图为正文主对照，新增晶圆台平台实测与十项功能比较，移除历史整机样本；[Nikon 设计](reports/semiconductor-equipment/2026-11-krf-vs-i-line/nikon-lens-supplement.md)改为补充。两件新公报的 57 页本地 MineU 稿及原件已入[资料库](materials/patents/README.md)。

- [ASML 产品与研发难度](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)补入两条产品线的研发和出货节点、870 机群 13 周表现、870B 的 7 处硬件及系统升级。逐项区分晶圆台、镜框、控制板、热调节工位与独立机柜，新增 ZEISS、ASML [两件专利原件及本地 MineU 逐页稿](materials/patents/README.md)。

- [光刻机调研](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)以 XT:400M 与 NXT:870 为主样本；区分标准与选配分辨率、ATP 负载及套刻定义，加入 XT:860N 同波长对照。历史样本保留作参照。
- [专利资料库](materials/patents/README.md)补齐两件 Nikon 日本公报，按原始页序用本地 MineU 转写，登记来源、页数、校对范围，并排展示两件专利的物镜剖面。
- [写作偏好](PREFERENCES.md)增加对比报告的并排呈现要求。

## 2026-11-02

- **单分支管理**　将报告写作、PDF 转写、专利归档和后续修订统一到 `main`。原有分支的内容和提交历史已整合，审阅改为[提交前检查](templates/pre-commit-checklist.md)。[整合记录](https://github.com/OpticsPan/Research_Report/commit/7252d63fba69baa5d28c866fa419f23c8f91c919)

- **PDF 来源转写**　将逐页转写、扫描页核对和原件定位纳入研究来源管理。作者按[首页流程](README.md#pdf-来源转写)处理 PDF，审阅者按 PR 清单核对覆盖范围和疑点。[PR #6](https://github.com/OpticsPan/Research_Report/pull/6)

- **报告写作偏好**　将已确认的[五条写作偏好](PREFERENCES.md#行业调研报告写作偏好)用于行业调研报告的撰写与审阅，涵盖摘要、段落、数字口径、图题图注和核算细节的放置。

- **单篇报告偏好**　在[光刻机报告](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md#本篇图表与行文约定)登记柱状图、时间箭头、多参数对照表和专利附图的使用场景，并从用户偏好页提供入口。

- **专利来源归档**　把每件专利的[逐页 Markdown](materials/patents/README.md#独立交付与引用)列为独立交付。光刻机报告的[来源表](reports/semiconductor-equipment/2026-11-krf-vs-i-line/sources.md)已直链两份逐页稿，并标明另两件待补原件。

- **专利原文归档**　补录 [Cymer 脉冲能量控制](materials/patents/EP1019992B1/fulltext.md)和 [ASML 扫描台测量](materials/patents/US6084673A/fulltext.md)两份按 PDF 原页组织的 Markdown，共 50 页。附图和公式可返回原页核对。

- **光刻机报告修订**　补充[官方数据底稿](reports/semiconductor-equipment/2026-11-krf-vs-i-line/official-data.md)和四件专利的技术摘录，加入线宽对照图与研发时间线。按专利实施例将 KrF 物镜最大 NA 从 0.55 改为 0.60，镜片计数维持 29 片。[报告与修订记录](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)

- **资料库**　建立[专利资料库](materials/patents/README.md)和全文转写模板，统一记录 PDF 来源、页码、权利要求和附图编号，方便跨报告复用与核查。

- **报告发布**　新增[KrF 与 i-line 光刻机工程难度对照](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)，分别核对同架构整机指标、投影物镜实施例和研发投入边界，登记板卡及机型级预算的资料缺口。

- **用户偏好管理**　新增[长期偏好登记表](PREFERENCES.md)，记录已确认的变更留痕要求。选题时可补充单篇要求，审阅时按对应范围核对。

- **变更管理**　建立本日志。读者可从[仓库首页](README.md)查看重要更新，提交者需在 [当时的 PR 清单](https://github.com/OpticsPan/Research_Report/blob/7252d63fba69baa5d28c866fa419f23c8f91c919/.github/pull_request_template.md)中核对登记情况。
- **目录与模板**　新增[报告目录](reports/README.md)、[报告模板](templates/report.md)和[来源表](templates/sources.md)，并为选题和审阅提供统一入口。作者可据此准备初稿，审阅者可逐项核查引用与统计口径。[提交 2d309c9](https://github.com/OpticsPan/Research_Report/commit/2d309c95cb8c1c671d766681c77a28b9e24bb497)
- **仓库初始化**　在首页约定选题、撰写、审阅、发布和修订流程，并说明数据口径、引用方式与公开材料的使用要求。[提交 8d6e3ed](https://github.com/OpticsPan/Research_Report/commit/8d6e3ed8f89cd51d609b941166353e0a6ff01344)
