# 仓库变更记录

本日志收录报告首次发布、影响关键数字或结论的修订，以及目录、模板和协作流程的调整。错字和排版调整可通过 Git 历史查询。

在同一份 PR 中把新条目写在最上方，按日期（YYYY-MM-DD）归档。每条写明改了什么、对读者或作者有什么影响，并链接对应的报告、PR 或提交。报告勘误还应在正文修订记录中保留原值、新值和修订依据。

## 2026-11-02

- **专利来源归档**　把每件专利的[逐页 Markdown](materials/patents/README.md#独立交付与引用)列为独立交付。光刻机报告的[来源表](reports/semiconductor-equipment/2026-11-krf-vs-i-line/sources.md)已直链两份逐页稿，并标明另两件待补原件。

- **专利原文归档**　补录 [Cymer 脉冲能量控制](materials/patents/EP1019992B1/fulltext.md)和 [ASML 扫描台测量](materials/patents/US6084673A/fulltext.md)两份按 PDF 原页组织的 Markdown，共 50 页。附图和公式可返回原页核对。

- **光刻机报告修订**　补充[官方数据底稿](reports/semiconductor-equipment/2026-11-krf-vs-i-line/official-data.md)和四件专利的技术摘录，加入线宽对照图与研发时间线。按专利实施例将 KrF 物镜最大 NA 从 0.55 改为 0.60，镜片计数维持 29 片。[报告与修订记录](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)

- **资料库**　建立[专利资料库](materials/patents/README.md)和全文转写模板，统一记录 PDF 来源、页码、权利要求和附图编号，方便跨报告复用与核查。

- **报告发布**　新增[KrF 与 i-line 光刻机工程难度对照](reports/semiconductor-equipment/2026-11-krf-vs-i-line/README.md)，分别核对同架构整机指标、投影物镜实施例和研发投入边界，登记板卡及机型级预算的资料缺口。

- **用户偏好管理**　新增[长期偏好登记表](PREFERENCES.md)，记录已确认的变更留痕要求。选题时可补充单篇要求，审阅时按对应范围核对。

- **变更管理**　建立本日志。读者可从[仓库首页](README.md)查看重要更新，提交者需在 [PR 清单](.github/pull_request_template.md)中核对登记情况。
- **目录与模板**　新增[报告目录](reports/README.md)、[报告模板](templates/report.md)和[来源表](templates/sources.md)，并为选题和审阅提供统一入口。作者可据此准备初稿，审阅者可逐项核查引用与统计口径。[提交 2d309c9](https://github.com/OpticsPan/Research_Report/commit/2d309c95cb8c1c671d766681c77a28b9e24bb497)
- **仓库初始化**　在首页约定选题、撰写、审阅、发布和修订流程，并说明数据口径、引用方式与公开材料的使用要求。[提交 8d6e3ed](https://github.com/OpticsPan/Research_Report/commit/8d6e3ed8f89cd51d609b941166353e0a6ff01344)
