# arcuscnc.com 内容缺口分析与新选题规划（v2 · 2026-11-08）

> 本版替换 v1。v1 只基于搜索引擎收录的约 35 个页面，把大量已写过的话题误判为空白。
> 本版基于：全站爬取（327 篇文章 + 42 页面 + 30 产品 + 9 服务 + 8 行业项目页）、
> `arcuscnc-sumrush.xlsx`（2,670 个排名词）、GSC 近 6 个月表现报告、
> 四个品类 US broad-match 关键词库（cleaning / cutting / marking / welding，去重后 3,772 词），
> 并遵循 `arcuscnc_writing_rules_v3.md`。
>
> `ArcusCNC 文章历史清单.md` 上传后内容为空（"共 0 / 0 篇"），本版的现有文章清单来自站点爬取，见附录 A。

---

## 一、现状诊断（先看问题，再看选题）

### 1. 流量结构：量在涨，但几乎全是信息词
- GSC 近 6 个月：14,160 次点击；近 30 天日均点击约 98，是半年前（约 43）的 2.3 倍，展示量同步翻倍。
- Semrush 估算流量中约 **90% 来自信息意图词**，前 20 个流量页面里 17 个是金属物性页（密度、熔点、弹性模量、铜 vs 青铜颜色……）。这类页面带量但几乎不带询盘。
- **真正接近询盘的页面在 GSC 里表现很好**：穿孔参数（488 点击，CTR 2.5%）、焦点设置（356）、电容传感器报错（320）、边缘缺陷（290）、空压机（237）、喷嘴过热（168，排名 4.9）。说明**故障排除和工艺类内容是这个站最有效的打法**，与写作规则一致。

### 2. 核心产品大词全部没进前 100
| 关键词 | 月搜索量（US）| KD | 现有对应页面 | 排名 |
|---|---|---|---|---|
| laser welder | 18,100 | 29 | /laser-welding-machines/ | 无 |
| laser welding machine | 6,600 | 27 | 同上 | 无 |
| laser cutting machine | 6,600 | 9 | /laser-cutting-machine/ | 无 |
| laser cleaning machine | 5,400 | 15 | /laser-cleaning-machine/ | 无 |
| laser marking machine | 1,900 | 11 | /laser-marking-machines/ | 无 |

页面本身检查过：可收录、canonical 正确、正文 1,700–2,500 词。问题不在"缺文章"，而在**权重分散 + 外链不足**（见下面第 4 点的重复页）。**不要再为这些大词新写文章。**

### 3. 站点地图过期
- `sitemap_index.xml` 中文章 lastmod 最新为 2026-06；博客列表里有 **107 篇文章不在站点地图中**（例：/laser-welding-aluminum/、/laser-marking-machines/、/press-brake-tonnage-calculator/）。
- GSC 显示这 107 篇都已有展示，即已被收录，**不是致命问题**，但新文章会被延迟发现。需检查 Rank Math 站点地图缓存/设置。
- /laser-cleaning-machine/ 同时存在于 post-sitemap 和 page-sitemap，存在文章与页面同 slug 冲突，需核实。

### 4. 关键词蚕食（重复页面组）——优先于写新文章处理
| 话题 | 重复页面 | 建议 |
|---|---|---|
| 激光清洗机价格 | laser-cleaner-price-guide / laser-cleaning-machine-price-analysis / laser-cleaner-machine-price / laser-cleaner-cost-breakdown / cheap-laser-cleaning-machine | 合并为 1 个价格枢纽页（按功率 100W–3000W 分表），其余 301 或改写为不同意图。GSC "han's laser cleaning machine price 1000w 1500w" 展示 3,334 次、0 点击，正是缺按功率报价表 |
| 激光切割机价格 | fiber-laser-cutter-price / laser-cutter-cost / buying-guide-fiber-laser-cutter-2025 / buying-a-fiber-laser-cutter | 价格 1 篇 + 选购 1 篇，统一报价口径 |
| 光纤 vs CO2 | fiber-laser-vs-co2-laser-cutter / fiber-vs-co2-laser | 合并 |
| 激光焊 vs TIG/MIG | laser-welder-vs-tig-mig / handheld-laser-welding-vs-tig / laser-welding-vs-arc-welding | 保留 2 篇并明确分工（手持 vs TIG；激光 vs 全部电弧焊），或合并 |
| 选购类文章 vs 产品页 | /laser-welding/（How to Choose）vs /laser-welding-machines/；/laser-marking/ vs /buying-a-laser-marking-machine/ vs /laser-marking-machines/ vs /laser-marking-machine-for-metal/ | 一个意图一个页面 |
| 铝切割 | laser-cutting-aluminum / cutting-aluminum-alloys / aluminum-laser-cutting-machine / air-cutting-aluminum-guide / assist-gas-for-aluminum-laser-cutting | "laser cut aluminum" 排第 1 的竟是 /laser-marking-aluminum-parts/（错页）；GSC "laser cutting aluminium" 展示 1,530 次、排名 24 |
| 不锈钢切割 | guide-to-cutting-stainless-steel / stainless-steel-laser-cutting-machine / laser-cutting-machine-stainless-steel-speed 等 | GSC "stainless steel laser cutting" 1,260 展示、排名 37.6；需确定一个主页面 |
| 黄铜切割 | laser-cutting-brass / copper-brass-laser-cutting-machine | GSC brass 相关词合计约 2,250 展示，排名 18–21 |
| 木材剥漆 | 7 篇（best-portable-laser-stripping-machine-for-wood、portable-laser-strippers-on-wood、laser-paint-stripper-on-hardwoods、laser-cleaner-machine-for-wood、log-cabin…、furniture…、heritage-building-wood-beam…）| 目前表现好，不再新增，只做内链梳理 |
| 金属物性 | density-of-iron / iron-metal-density / density-of-fe；3 篇 6061 导热；3 篇铜熔点 | 合并同义页，并在物性页加入指向工艺/产品页的上下文链接 |

---

## 二、新文章选题（已逐条核对 327 篇，确认无专门文章）

格式说明：搜索量/KD 为 Semrush US 数据（月搜索量 / 难度）；"防蚕食"一栏说明与现有最近文章的区别。全部为中/底漏斗，符合规则第二条。

### P1：数据明确、缺口确认、离询盘近（建议前 6 周完成）

| # | 建议标题（英文）| 建议 URL | 主关键词（量/KD）| 关键词集群总量 | 类型 | 防蚕食 / 依据 |
|---|---|---|---|---|---|---|
| 1 | How to Evaluate Chinese Laser Cleaning Machine Manufacturers | /laser-cleaning-machine-manufacturers-china/ | top fiber laser cleaning machine manufacturers china 2024 reviews 1,300/5 | 100 词 / 2,530 | 厂商指南 | 现有 /chinese-fiber-laser-manufacturers/ 只讲切割。**GSC 该查询展示 6,189 次、排名 8.4、0 点击**，Google 已在测试我们，但没有匹配页面。按规则写评判框架和自查清单，不点名排名竞品 |
| 2 | Laser Cutting Software: CAD, CAM, Nesting and Controller Software Explained | /laser-cutting-software/ | laser cutting software 1,900/20 | 11 词 / 3,840 | 选型 | 现有只有 /nesting-software-strategies-stainless/（不锈钢套料技巧）和套料计算器，没有软件选型页。覆盖设计软件、CAM/套料、机床控制系统三层，以及与控制系统的兼容性 |
| 3 | Laser Marking Spray vs Fiber Laser Marking: Cost per Part and When Each Makes Sense | /laser-marking-spray-vs-fiber-laser/ | laser marking spray 720/15；cermark laser marking spray 390/14；black laser marking spray 170/5 | 66 词 / 3,230 | 比较 | 全站零覆盖。读者是用 CO2/二极管激光 + 喷剂打金属的工厂，正考虑升级到光纤打标机，属于升级型询盘。须写清喷剂更适合的场景 |
| 4 | Best Handheld Laser Welder: An Evaluation Framework for Fabrication Shops | /best-handheld-laser-welder/（不带年份）| best laser welder 390/30；best laser welder for the money 140/11；best handheld laser welder 110/2 | 7 词 / 970 | 选购（常青）| 无 "best" 类焊机文章。按规则第十三条：去年份、不点名排名，给评判维度表（功率、送丝、冷却方式、安全联锁、售后）|
| 5 | Laser Cleaning Machine Rental vs Buying vs Outsourcing: Cost Comparison | /laser-cleaning-machine-rental-vs-buy/ | laser cleaning service 210/15；laser cleaning machine rental 170/0；laser cleaner rental 110/7 | 23 词 / 1,130 | 比较 / 成本 | /mobile-rust-removal-business/ 是创业角度，/lease-a-laser-machine/ 讲切割机租赁。本文给工厂决策者：按年清洗面积的租/买/外包盈亏点（Hypothetical example）|
| 6 | Laser Cutting Tolerances and Kerf Width by Material, Thickness and Power | /laser-cutting-tolerances-kerf/ | laser cutting smallest kerf 320/17；laser cutting tolerances 140/18；tolerance of laser cutting 110/9 | 10 词 / 960 | 工况选型（查表型）| /tolerance-definition-in-engineering/ 是通用定义页。本文是激光切割专用数据表，可被报价、设计、质检人员直接引用，适合 AI 引用 |
| 7 | Laser Welding for Medical Devices: Materials, Joint Types and Validation Requirements | /laser-welding-medical-devices/ | laser welding medical devices 140/10；medical device laser welding 110/10 | 6 词 / 460 | 行业应用 | 现有 /laser-marking-medical-devices/ 讲打标，行业页 /lq-project/…medical-devices… 偏切割。本文讲焊接：316L、钛、密封焊、验证（IQ/OQ/PQ）。**须写明手持光纤焊机不适合精密医疗微焊**（诚实局限）。/fiber-laser-welding-machine-applications/ 只是一句话带过，不冲突 |
| 8 | 3D (Dynamic Focus) Laser Marking Machines: When a 2D Galvo Is Not Enough | /3d-laser-marking-machine/ | 3d laser marking machine 260/14；3d laser marking 210/7 | 5 词 / 580 | 工况选型 | 现有 /galvo-laser-marking-vs-gantry/、/rotary-laser-marking-for-cylindrical-parts/ 都没讲动态聚焦；/laser-marking-focus/ 是聚焦故障排查，应链接过去而非重复写。低 KD、商业意图 |

### P2：有数据支撑、需求中等（第 7–12 周）

| # | 建议标题 | 建议 URL | 主关键词（量/KD）| 集群总量 | 类型 | 防蚕食 / 依据 |
|---|---|---|---|---|---|---|
| 9 | Laser Marking Machine Types: Desktop vs Split vs Enclosed vs Handheld Workstations | /laser-marking-machine-types/ | laser marking workstation 110/19；desktop fiber laser marking machine 110/27 | 18 词 / 800 | 选型 | /portable-laser-marking-machine/ 只讲便携式 |
| 10 | Laser Marking Titanium: Black, Color and Deep Marks for Medical and Aerospace Parts | /laser-marking-titanium/ | laser marking titanium 170/5；color laser marking machine 140/18 | 21 词 / 970 | 工艺 | /mopa-fiber-laser-marking/ 讲光源，本文讲钛材工艺和验证；两篇互链，避免重复写 MOPA 原理 |
| 11 | Laser Welding Gun Parts: Nozzles, Protective Lens, Wire Feed Tips and Replacement Intervals | /laser-welding-gun-parts/ | laser welding gun 320/18；laser welder gun 170/17 | 2 词 / 490 | 维护 / 故障 | /laser-spare-parts/ 是切割配件，/laser-welding-cost-consumable/ 讲成本。本文讲焊枪结构和更换判断 |
| 12 | Laser Cutting Table Slats: Wear, Cleaning and Replacement | /laser-cutting-table-slats/ | laser cutting table 390/10；laser cutting table for steel 110/12 | 5 词 / 640 | 维护 | /dual-exchange-table-laser-cutter/ 讲交换台选型。注意 "laser cutting table" 有部分产品意图，开头需兼顾 |
| 13 | Laser Welding Training and Operator Certification: What Your Team Needs | /laser-welding-training/ | laser welding training 90/16；laser welding course 70/16；laser welding certification 50/8 | 3 词 / 210 | 采购前顾虑 | 零覆盖；可附设备交付培训内容（须如实，不承诺未提供的认证）|
| 14 | Used Laser Welder: Inspection Checklist and Hidden Costs | /used-laser-welder/ | used laser welder for sale 110/8 | 3 词 / 230 | 选购 | 现有新机 vs 二手的两篇都只讲切割机 |
| 15 | Green Laser (532 nm) Marking and Welding: Copper, Gold and Thin Foils | /green-laser-marking-welding/ | green laser marking machine 110/5；green laser marking 90/6 | 4 词 / 250 | 工况选型 | 与 /laser-welding-battery/ 的铜焊内容衔接，不重复电池工艺细节 |

### P2（待补数据）：折弯机集群
已有 12 篇（操作、厂商、欧式模具、维护、模具设计、折弯半径、吨位计算器、K 因子、展开计算、Z 折……），以下话题尚无专门文章：
- CNC Press Brake Buying Guide & Price（选购 + 价格，底漏斗）
- Hydraulic vs Electro-Hydraulic vs Servo-Electric Press Brake（比较）
- Press Brake CNC Controllers Compared（控制系统对比，仅用公开规格）
- Springback in Sheet Metal Bending: Causes and Compensation（故障排除）
- Air Bending vs Bottoming vs Coining（比较）
- Press Brake Safety: Light Curtains, Laser Guards and Two-Hand Controls（安全）

GSC 佐证："press brake manufacturer(s)" 合计 1,039 展示、排名 29–36；"cnc bending" 502 展示、排名 32。**上传的关键词库里没有折弯机品类**，建议补导出一份 `press brake broad-match US`，再确定顺序。

### P3：可写但优先级低
| 选题 | 数据 | 说明 |
|---|---|---|
| Laser Welding Titanium | 110/22 | 小众，可放在医疗或航空文章中 |
| Can a Fiber Laser Weld Plastic? | 集群 320，KD 6–17 | 公司不卖塑料焊接设备，只能写"不能，以及需要什么设备"，转化低 |
| Small / Mini Laser Welder | 集群 780；small laser welding machine price 390/29 | 与 /portable-laser-welder/ 意图接近，蚕食风险高，建议先优化 portable 页 |

---

## 三、优化现有页面（不写新文章，收益可能更快）

| 现有页面 | 机会（数据）| 动作 |
|---|---|---|
| /chinese-fiber-laser-manufacturers/ | GSC 展示 36,382、排名 12.4、CTR 0.8% | 改 Title/Meta，补"评估清单"表格，争取进前 10 |
| /laser-cleaning-machine-price-analysis/（或合并后的枢纽页）| GSC 展示 41,567、排名 9.4；"3000w laser cleaning machine price" 880/9，按功率报价词集群约 5,640 | 加 100W–3000W 分功率价格表，然后合并其余 4 篇价格页 |
| /qr-code-laser-marking-on-metal/ | "qr code laser marking" 880/KD1，未排名 | 用目标词重写开头和 H2，补数据矩阵/UDI 内容 |
| /laser-marking-plastic/ | 集群 1,630，KD 2–15，未排名 | 同上 |
| /laser-welding-aluminum/ | 590/KD4，排名 26–34 | 补参数表和 FAQ |
| /laser-welding-power/ | 排名 7.3；"1500w laser welding" 260/5、"1500w laser welder" 140/6 未排名 | 增加 1500W / 2000W / 3000W 能焊多厚的对照表（不新开页）|
| /laser-marking-supplier/ | 厂商类词集群 1,810，未排名 | 标题改为面向 "laser marking machine manufacturer" |
| /press-brake-manufacturers/ | 1,039 展示，排名 29–36 | 补厂商评估维度表 |
| /tips-for-cutting-galvanized-steel/ | GSC 合计约 900 展示，排名 14–22 | 补参数表和 FAQ |
| /laser-vs-plasma-cost/、/cutting-thick-steel/、/tips-for-cutting-hardox/、/cutting-rusty-metal/、/laser-cutting-environmental-setup-requirements/ | GSC 出现大量 AI 搜索式长问句并排在 2–8 位但 0 点击，例如 "what is the best cutting process for 25 mm mild steel"、"facility requirements for plasma and fiber laser…"、"fastest ROI for a small or midsize fabrication shop" | 把这些问题原样做成 H2/H3 或 FAQ，首句直接给结论（规则第三、四条），提高被 AI 摘要引用的概率 |
| 4 个产品主页面 | 大词无排名 | 合并重复的选购文章、统一内链锚文本、做外链；不新写 |

---

## 四、不建议写的方向
- **CO2 / 爱好者类词**（acrylic、wood、plywood、laser cut files、ideas、ornaments、near me）：切割词库中量很大，但与工业金属设备无关。
- **顶漏斗定义类**（laser beam welding 3,600、what is laser welding、laser marking machine benefits 2,900、fiber laser marking advantages 1,600）：规则明确降级，AI 会直接回答。
- **更多金属物性页**：已有 60 多篇，带量不带询盘。应该给现有物性页加指向工艺/产品页的链接，而不是继续扩写。
- **地区 + 城市词**（如 "laser marking stainless steel irvine ca"）：本地服务意图，不适合设备厂。

---

## 五、建议排期（每周 2 篇，以本站目前的更新节奏可以支持）

| 周 | 内容 |
|---|---|
| 第 0 周 | 修站点地图；清洗机价格 5 篇合并；改 /chinese-fiber-laser-manufacturers/ 标题 |
| 第 1 周 | #1 中国清洗机厂商评估、#2 激光切割软件 |
| 第 2 周 | #3 打标喷剂 vs 光纤、#6 公差与切缝表 |
| 第 3 周 | #4 最佳手持焊机评估框架、#5 清洗机租/买/外包 |
| 第 4 周 | #7 医疗器械激光焊接、#8 3D 动态聚焦打标 |
| 第 5 周 | 优化：QR 打标、塑料打标、焊铝、焊接功率页 |
| 第 6 周 | 优化：AI 长问句 FAQ 补写（5 篇）；合并光纤 vs CO2、焊接 vs TIG 重复页 |
| 第 7–10 周 | #9–#15（P2）|
| 第 11–12 周 | 折弯机集群（补关键词数据后）|

每篇写作前按规则第一条完成 Pre-writing Brief，"防蚕食检查"一项可直接引用本文第二节的防蚕食列。

---

## 附录 A：现有内容规模（2026-11-08 爬取）
- 文章 327 篇：站点地图内 220 篇，站点地图外 107 篇（博客分类分页中可访问，GSC 均有展示）
- 页面 42、产品 30、服务 9、行业项目 8（汽车/EV、能源、农业、航空、健身器材、厨卫、钣金 HVAC、医疗）
- 博客分类：laser-machine-blog、laser-welding-blog、laser-cleaning-blog、cnc-press-brake、laser-marking-machine、study-case

## 附录 B：方法说明
- 缺口判定：关键词在 Semrush 排名表中无排名或排名 >20，且 327 篇文章 slug 中没有匹配话题；P1 选题另外用站内全文搜索复核：相关词只在其他文章正文中顺带出现，没有专门文章。
- 搜索量为 Semrush US 月均值，仅代表美国市场；GSC 显示印度、加拿大、澳大利亚、英国也有可观流量，实际总需求更高。
- 本文所有数字均来自上传的数据文件或站点爬取；未核实的厂商信息、认证和价格在写作时须按规则第十五条列入 Items Pending Verification。
