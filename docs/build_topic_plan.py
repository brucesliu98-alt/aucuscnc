"""Build the new-topic series plan (xlsx + md) for arcuscnc.com.

Data sources: Semrush broad-match keyword exports (US, 2026-11-08), Semrush
organic positions export, GSC performance export, and a full crawl of the
327 published posts (used for the anti-cannibalization check).
Run: python3 docs/build_topic_plan.py
"""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# (series, ep, priority, week, title, core_kw, core_vol_kd, secondary, cluster_vol,
#  url, funnel, type, link_to, evidence)
S1 = "S1 激光切割软件与编程"
S2 = "S2 切割精度、自动化与渠道"
S3 = "S3 激光焊接工艺与质量"
S4 = "S4 激光焊机选购"
S5 = "S5 激光清洗：功率段与采购"
S6 = "S6 激光打标：工艺与机型"
S7 = "S7 数控折弯机"

ROWS = [
    # ---------------- S1 ----------------
    (S1, 1, "P1", 1,
     "Laser Cutting Software Explained: Design, CAM/Nesting and Controller Software for Metal Shops",
     "laser cutting software", "1,900 / 20",
     "design software for laser cutting (390/18); laser cutting design software (390/21); laser cutting machine software (390/17); software for laser cutting (260/20)",
     "3,840", "/laser-cutting-software/", "中", "选型",
     "/nesting-software-strategies-stainless/; /sheet-nesting-calculator/; /fly-cutting/",
     "全站无软件选型文章；现有套料文章只讲不锈钢套料技巧"),
    (S1, 2, "P1", 2,
     "CypCut Parameter Setup: Layers, Piercing, Lead-ins and Cutting Process Libraries",
     "cypcut parameters", "GSC：46 展示 / 排名 8.9",
     "cypcut (GSC 排名 2.7); cypcut flycut (GSC 75 展示)",
     "无 Semrush 数据", "/cypcut-parameter-guide/", "中", "教程 / 故障",
     "/fly-cutting/; /frog-jump-cutting/; /optimizing-laser-piercing-parameters-for-thick-plate-cutting/",
     "GSC 已出现 CypCut 查询且排名靠前，但没有对应专题页；面向已购机用户"),
    (S1, 3, "P2", 9,
     "Free vs Paid Laser Cutting Software: What Free Tools Can and Cannot Do for Production Metal Cutting",
     "free software for laser cutting", "110 / 18",
     "laser cutting software free download (50/22); free laser cutting software (50/17)",
     "210", "/free-laser-cutting-software/", "中", "比较",
     "/laser-cutting-software/（S1-1）",
     "从生产效率、套料率、控制系统兼容性评判，过滤爱好者流量"),
    (S1, 4, "P3", 16,
     "Preparing DXF Files for Fiber Laser Cutting: Kerf Compensation, Micro-joints and Common-Line Cutting",
     "dxf file for laser cutting", "50 / 21",
     "dxf files for laser cutting (170/23)",
     "约 220（排除下载类）", "/dxf-file-preparation-laser-cutting/", "中", "教程",
     "/laser-cutting-software/; /laser-cutting-tolerances-kerf/",
     "该词簇主要是下载文件意图，本文只吃工程意图，优先级低"),

    # ---------------- S2 ----------------
    (S2, 1, "P1", 1,
     "Laser Cutting Tolerances and Kerf Width by Material, Thickness and Laser Power",
     "laser cutting tolerances", "140 / 18",
     "laser cutting smallest kerf (320/17); tolerance of laser cutting (110/9); what is kerf in laser cutting (90/18); laser cutting kerf (70/17)",
     "960", "/laser-cutting-tolerances-kerf/", "中", "查表型 / 工况选型",
     "/tolerance-definition-in-engineering/; /fix-laser-cutting-edge-taper-stainless/",
     "现有 tolerance 文章是通用工程定义；本文给激光切割专用数据表，适合被 AI 引用"),
    (S2, 2, "P1", 3,
     "Laser Cutting Automation: Loading/Unloading Systems, Material Towers and When They Pay Off",
     "laser cutting automation", "210 / 15",
     "automatic loading and unloading laser cutting; laser cutting storage tower（长尾，无单独数据）",
     "210+", "/laser-cutting-automation/", "底", "选型 / ROI",
     "/dual-exchange-table-laser-cutter/; /laser-cutting-roi/; /fiber-laser-roi-calculator/",
     "现有自动化文章只覆盖焊接和打标；切割自动化为空白"),
    (S2, 3, "P2", 8,
     "Laser Cutting Table Slats: Wear Signs, Cleaning and Replacement Intervals",
     "laser cutting table", "390 / 10",
     "laser cutting table for steel (110/12); cnc laser cutting table (70/10)",
     "640", "/laser-cutting-table-slats/", "中", "维护 / 故障",
     "/dual-exchange-table-laser-cutter/; /metal-laser-cutting-machine-maintenance-checklist/",
     "该词有部分产品意图，开头需先回答台面选型再讲维护"),
    (S2, 4, "P2", 12,
     "How to Become a Fiber Laser Machine Distributor: Margins, Service Obligations and Supplier Evaluation",
     "laser cutting machine distributor", "140 / 22",
     "laser marking machine distributor (20); laser marking machine dealer (10)",
     "170", "/laser-cutting-machine-distributor/", "底", "厂商 / 渠道指南",
     "/partners-clients/; /chinese-fiber-laser-manufacturers/",
     "面向经销商的招商内容，询盘价值高；全站零覆盖"),

    # ---------------- S3 ----------------
    (S3, 1, "P1", 2,
     "How Strong Is a Laser Weld? Tensile, Bend and Macro-Etch Results Compared with TIG",
     "is laser welding strong", "110 / 20",
     "how strong is laser welding (50/11); laser welding strength (50/10)",
     "210", "/laser-weld-strength/", "中", "比较 / 验证",
     "/laser-welder-vs-tig-mig/; /laser-welding-heat-affected-zone/",
     "当前由其他页面排在第 74 位，没有对应文章；测试数据须引用公开标准，不能编造"),
    (S3, 2, "P1", 4,
     "Laser Welding Helmets and Safety Glasses: OD Ratings, Wavelength and Why Arc Helmets Are Not Enough",
     "laser welding helmet", "140 / 2",
     "laser welding helmets (90/2); laser welding glasses（长尾）",
     "230", "/laser-welding-helmet/", "中", "选型 / 安全",
     "/laser-welding-safety/; /fiber-laser-radiation-safety/",
     "KD 只有 2；现有安全文章是总论，不讲防护装备选型"),
    (S3, 3, "P1", 4,
     "Laser Welding for Medical Devices: Materials, Joint Types and Process Validation",
     "laser welding medical devices", "140 / 10",
     "medical device laser welding (110/10); medical laser welding (70/9); laser welding machine for medical device industry (50/6)",
     "460", "/laser-welding-medical-devices/", "中", "行业应用",
     "/laser-marking-medical-devices/; /lq-project/advanced-laser-processing-for-medical-devices-surgical-implants/",
     "现有医疗内容是打标和行业页；须写明手持焊机不适合精密医疗微焊"),
    (S3, 4, "P2", 7,
     "Conduction vs Keyhole vs Wobble Laser Welding: Which Mode for Your Joint and Thickness",
     "keyhole laser welding", "90 / 11",
     "types of laser welding (70/16)",
     "160", "/keyhole-vs-conduction-laser-welding/", "中", "比较",
     "/laser-welding-beam-focus/; /laser-welding-power/",
     "工艺模式选择，现有文章没有专门讲"),
    (S3, 5, "P2", 10,
     "Laser Weld Inspection: Visual, Dye Penetrant, Ultrasonic and In-Process Monitoring",
     "laser weld inspection", "70 / 15",
     "laser weld quality control（长尾）",
     "70+", "/laser-weld-inspection/", "中", "质量 / 故障",
     "/laser-welding-defects/; /laser-weld-strength/（S3-1）",
     "与焊接缺陷文章分工：缺陷讲成因和修正，本文讲检测方法和验收"),
    (S3, 6, "P3", 15,
     "Laser Welding Titanium: Shielding, Contamination Control and Joint Design",
     "laser welding titanium", "110 / 22",
     "", "110", "/laser-welding-titanium/", "中", "材料工艺",
     "/laser-welding-shielding-gas/; /laser-welding-medical-devices/（S3-3）",
     "现有焊接材料文章覆盖铝、不锈钢、黄铜、镀锌板，缺钛"),
    (S3, 7, "P3", 16,
     "Laser Cladding vs Laser-Arc Hybrid Welding: Where Each Process Fits",
     "laser deposition welding", "70 / 9",
     "laser hybrid welding (70/15); laser clad welding (30/12)",
     "180", "/laser-cladding-vs-hybrid-welding/", "顶–中", "比较",
     "/laser-welding-vs-arc-welding/",
     "如公司不提供这两类设备，应写成诚实说明型文章"),

    # ---------------- S4 ----------------
    (S4, 1, "P1", 1,
     "Best Handheld Laser Welder: An Evaluation Framework for Fabrication Shops",
     "best laser welder", "390 / 30",
     "best laser welding machine (210/22); best laser welder for the money (140/11); laser welder reviews (110/3); best handheld laser welder (110/2)",
     "1,130", "/best-handheld-laser-welder/", "底", "选购（常青）",
     "/laser-welding-supplier-evaluation-checklist/; /laser-welding-power/; /3-in-1-laser-machines/",
     "无 best 类焊机文章；按规则第十三条不带年份、不给竞品排名"),
    (S4, 2, "P2", 6,
     "Cheap Laser Welders: What You Give Up at the Lowest Price Points",
     "cheap laser welder", "260 / 12",
     "cheapest laser welder (140/10); low cost laser welder (90/20)",
     "490", "/cheap-laser-welder/", "底", "选购 / 风险",
     "/3-in-1-laser-welding-machine-price/; /laser-welder-price-roi-case-study/",
     "清洗机已有 cheap 页，焊机没有；价格只引用统一口径"),
    (S4, 3, "P2", 8,
     "Mini and Benchtop Laser Welders: Jewelry, Mold Repair and Small-Part Applications",
     "small laser welding machine price", "390 / 29",
     "mini laser welding machine (110/7); small laser welder (90/14); benchtop laser welder (90/6); desktop laser welder (70/21)",
     "780", "/mini-laser-welder/", "底", "选型",
     "/portable-laser-welder/; /laser-welding-jewelry/",
     "须与手持便携焊机区分（台式脉冲 vs 手持连续光），防止和 portable 页互相抢词"),
    (S4, 4, "P2", 11,
     "Used Laser Welder: Inspection Checklist, Laser Source Hours and Hidden Costs",
     "used laser welder for sale", "110 / 8",
     "used laser welding machine for sale (70/11); used laser welder (50/8)",
     "230", "/used-laser-welder/", "底", "选购 / 风险",
     "/used-laser-cutting-machine/; /fiber-laser-for-sale-new-vs-used/",
     "现有二手文章只讲切割机"),
    (S4, 5, "P2", 13,
     "Laser Welding Training and Operator Certification: What Your Team Needs Before Production",
     "laser welding training", "90 / 16",
     "laser welding course (70/16); laser welding classes (70/16); laser welding certification (50/8)",
     "280", "/laser-welding-training/", "中", "采购前顾虑",
     "/laser-welding-safety/; /service/after-sales-services-maintenance/",
     "全站零覆盖；不能承诺公司未提供的认证"),

    # ---------------- S5 ----------------
    (S5, 1, "P1", 2,
     "How to Evaluate Chinese Laser Cleaning Machine Manufacturers: Factory Checks and Spec Verification",
     "top fiber laser cleaning machine manufacturers china", "1,300 / 5",
     "laser cleaning machine manufacturer (110/27); laser cleaning machine supplier (40); china laser cleaning machine manufacturers (30)",
     "2,530", "/laser-cleaning-machine-manufacturers-china/", "底", "厂商指南",
     "/chinese-fiber-laser-manufacturers/; /laser-cleaning-machine-specs/",
     "GSC 已有 6,189 次展示、排名 8.4、0 点击，但没有对应页面；现有中国厂商文章只讲切割"),
    (S5, 2, "P1", 3,
     "3000W Laser Cleaning Machine: Coverage Rate, Heavy Rust and Coating Removal, and Price Range",
     "3000w laser cleaning machine price", "880 / 9",
     "3000w sup fiber laser cleaning rust removal machine (140/0); 3000 watt laser cleaner (110/8); 3000w continuous laser cleaning machine (90/6); 3000w laser cleaning machine (90/23)",
     "约 1,400", "/3000w-laser-cleaning-machine/", "底", "单功率段选型",
     "/laser-rust-removal-gun-wattage-guide/（作为功率总览页）; 清洗机价格枢纽页; /laser-cleaning-for-marine/",
     "单功率段深度页。功率总览页负责横向比较，本页讲该功率能做什么；价格只给区间并链接枢纽页"),
    (S5, 3, "P1", 5,
     "2000W Laser Cleaner: What It Removes, How Fast, and When to Step Up to 3000W",
     "2000w laser cleaner", "140 / 0",
     "2000w sup fiber laser cleaning rust removal machine (260/2); 2000 watt laser cleaner (140/0); 2000w continuous laser cleaning machine (90/1); laser cleaning machine 2000w (70/0)",
     "约 750", "/2000w-laser-cleaner/", "底", "单功率段选型",
     "/laser-rust-removal-gun-wattage-guide/; /3000w-laser-cleaning-machine/（S5-2）",
     "KD 0–2，竞争极低"),
    (S5, 4, "P1", 5,
     "1000W vs 1500W Laser Cleaner: Rust Removal Speed, Substrate Risk and Typical Applications",
     "1500w sup fiber laser cleaning rust removal machine", "320 / 0",
     "1000 watt laser cleaner (110/12); 1000w laser cleaner (70/10); 1000w pulse laser cleaning machine (70/0); 1500w laser cleaning machine (50/0)",
     "约 750", "/1500w-laser-cleaner/", "底", "单功率段选型",
     "/laser-rust-removal-gun-wattage-guide/; /pulsed-laser-cleaner-vs-continuous-wave/",
     "KD 0–12"),
    (S5, 5, "P2", 7,
     "300W Pulsed Laser Cleaner: Precision Cleaning Jobs It Handles and Its Limits",
     "300w pulsed 2d laser cleaning machine", "170 / 0",
     "300 watt laser cleaner (140/1); 300w pulse laser cleaning machine (170/2); 300w pulsed laser cleaning machine (40/0)",
     "约 520", "/300w-pulsed-laser-cleaner/", "底", "单功率段选型",
     "/handheld-pulsed-laser-cleaning-machine/; /product/backpack-pulse-laser-cleaning-machine-300w/",
     "须与 handheld pulsed 文章区分：那篇讲形态，本篇讲 300W 能力边界"),
    (S5, 6, "P1", 3,
     "Laser Cleaning Machine Rental vs Buying vs Outsourcing: Break-Even by Annual Cleaning Area",
     "laser cleaning machine rental", "170 / 0",
     "laser cleaning service (210/15); laser cleaning services (170/15); laser cleaner rental (110/7); laser welder rental (50/11)",
     "1,180", "/laser-cleaning-machine-rental-vs-buy/", "中", "比较 / 成本",
     "/mobile-rust-removal-business/; /laser-cleaning-cost-calculator/; /lease-a-laser-machine/",
     "现有文章是创业角度和切割机租赁；本文面向工厂决策"),
    (S5, 7, "P2", 10,
     "Laser Cleaning Gun Parts: Protective Lens, Scan Width Settings and Replacement Intervals",
     "laser cleaning tool", "140 / 20",
     "laser cleaning gun (110/19); laser cleaner gun (70/15); laser metal cleaning gun (40)",
     "430", "/laser-cleaning-gun/", "中", "维护 / 选型",
     "/laser-cleaning-machine-lens-overheating/; /laser-rust-removal-gun-no-output/",
     "现有文章是故障排查，本篇讲清洗枪结构、参数和耗材"),

    # ---------------- S6 ----------------
    (S6, 1, "P1", 2,
     "Laser Marking Spray vs Fiber Laser Marking: Cost per Part and When Each Makes Sense",
     "laser marking spray", "720 / 15",
     "cermark laser marking spray (390/14); black laser marking spray (170/5); laser marking spray for stainless steel (140/4); laser marking spray alternative (90/5); co2 laser marking spray (70/5)",
     "3,230", "/laser-marking-spray-vs-fiber-laser/", "中", "比较",
     "/fiber-laser-marking-machine-vs-co2/; /laser-marking-on-stainless-steel/",
     "全站零覆盖；读者是用 CO2 或二极管激光加喷剂打金属、正考虑换光纤的工厂"),
    (S6, 2, "P1", 4,
     "3D Dynamic Focus Laser Marking: When a Standard 2D Galvo Is Not Enough",
     "3d laser marking machine", "260 / 14",
     "3d laser marking (210/7); laser marking machine 3d (140/6); 3d laser marking software (70/31)",
     "720", "/3d-laser-marking-machine/", "中", "工况选型",
     "/galvo-laser-marking-vs-gantry/; /rotary-laser-marking-for-cylindrical-parts/; /laser-marking-focus/",
     "laser-marking-focus 是聚焦故障排查，只做链接，不重复"),
    (S6, 3, "P2", 6,
     "Laser Marking Machine Types: Desktop, Split, Enclosed, Handheld and Inline Compared",
     "laser marking workstation", "110 / 19",
     "desktop fiber laser marking machine (110/27); mini laser marking machine (110/22); small laser marking machine (90/15); desktop laser marking machine (90/34)",
     "800", "/laser-marking-machine-types/", "中", "选型",
     "/portable-laser-marking-machine/; /inline-laser-marking-systems-for-automated/; /buying-a-laser-marking-machine/",
     "现有文章只讲便携式和产线式，没有整体机型对比"),
    (S6, 4, "P2", 9,
     "Color Laser Marking on Titanium and Stainless Steel: Process Window and Durability",
     "laser marking titanium", "170 / 5",
     "color laser marking (140/22); color laser marking machine (140/18); colour laser marking machine (90/15); color laser marking on metal (70/15)",
     "970", "/color-laser-marking-titanium/", "中", "材料工艺",
     "/mopa-fiber-laser-marking/; /laser-marking-medical-devices/",
     "MOPA 文章讲光源，本文讲材料工艺窗口和耐久性"),
    (S6, 5, "P2", 11,
     "Green Laser (532 nm) Marking: Copper, Gold and Thin Foils Compared with Fiber and UV",
     "green laser marking machine", "110 / 5",
     "green laser marking (90/6); green laser marker (30)",
     "250", "/green-laser-marking/", "中", "工况选型",
     "/fiber-vs-uv-laser-marking/; /laser-marking-copper-and-brass/",
     "KD 5–6"),
    (S6, 6, "P3", 14,
     "Laser Marking Carbide Cutting Tools and Inserts: Contrast, Depth and Coating Effects",
     "carbide laser marking", "70 / 11",
     "", "70", "/laser-marking-carbide-tools/", "中", "行业应用",
     "/laser-marking-bearings-gears/; /laser-marking-depth-explained/",
     "刀具行业零覆盖"),
    (S6, 7, "P3", 15,
     "Laser Marking Powder-Coated and Painted Parts: Coating Removal Without Substrate Damage",
     "laser marking powder coating", "70 / 15",
     "", "70", "/laser-marking-powder-coating/", "中", "材料工艺",
     "/laser-marking-aluminum-parts/; /laser-coating-removal/",
     "涂层件打标零覆盖"),

    # ---------------- S7 ----------------
    (S7, 1, "P2", 6,
     "CNC Press Brake Buying Guide: Tonnage, Bed Length, Axes and Price Ranges",
     "cnc press brake", "需补 Semrush 数据",
     "press brake manufacturer(s)（GSC 合计约 1,500 展示，排名 29–36）; cnc bending machine（GSC 189 展示）",
     "待补", "/cnc-press-brake-buying-guide/", "底", "选购 / 价格",
     "/press-brake-manufacturers/; /press-brake-tonnage-calculator/; /product/cnc-press-brake/",
     "GSC 显示 Google 已把网站和折弯机厂商词关联，但只有厂商名单文章，没有选购和价格文章"),
    (S7, 2, "P2", 7,
     "Hydraulic vs Electro-Hydraulic vs Servo-Electric Press Brake: Speed, Accuracy and Running Cost",
     "hydraulic vs electric press brake", "需补数据",
     "servo electric press brake; electro-hydraulic press brake", "待补",
     "/hydraulic-vs-servo-electric-press-brake/", "中", "比较",
     "/cnc-bending-machine/; /cnc-press-brake-buying-guide/（S7-1）", "零覆盖"),
    (S7, 3, "P2", 9,
     "Springback in Sheet Metal Bending: Causes by Material and How to Compensate",
     "springback sheet metal", "需补数据",
     "springback compensation; stainless steel springback", "待补",
     "/sheet-metal-springback/", "中", "故障排除",
     "/bend-radius-in-sheet-metal-work/; /k-factor-calculator/", "零覆盖"),
    (S7, 4, "P2", 12,
     "Air Bending vs Bottoming vs Coining: Tonnage, Accuracy and Tooling Cost",
     "air bending vs bottoming", "需补数据",
     "coining sheet metal; bottom bending", "待补",
     "/air-bending-vs-bottoming-vs-coining/", "中", "比较",
     "/bending-force-in-press-tools/; /press-brake-die-design-basics/", "零覆盖"),
    (S7, 5, "P3", 14,
     "Press Brake CNC Controllers Compared: What Each Controller Tier Gives the Operator",
     "press brake controller", "需补数据",
     "delem press brake; cnc press brake controller", "待补",
     "/press-brake-cnc-controller/", "中", "比较",
     "/press-brake-operation/", "只用公开规格，不编造竞品参数"),
    (S7, 6, "P3", 16,
     "Press Brake Safety: Light Curtains, Laser Guards and Two-Hand Controls",
     "press brake safety", "需补数据",
     "press brake light curtain; press brake guarding", "待补",
     "/press-brake-safety/", "中", "安全 / 合规",
     "/press-brake-operation/; /press-bender-machine-maintenance/", "零覆盖"),
]

HEAD = ["系列", "集", "优先级", "建议周次", "英文标题（建议）", "核心关键词", "核心词 量/KD（US）",
        "次要关键词（量/KD）", "关键词簇总量", "建议 URL", "漏斗", "文章类型", "内链至（已有页面）", "数据依据 / 防蚕食说明"]


def build_xlsx(path):
    wb = Workbook()
    ws = wb.active
    ws.title = "新选题规划"
    ws.append(HEAD)
    for r in ROWS:
        ws.append(list(r))
    head_fill = PatternFill("solid", fgColor="1F3A5F")
    pri_fill = {"P1": "FDE2E1", "P2": "FFF4D6", "P3": "EEF2F6"}
    thin = Side(style="thin", color="C9D1DB")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head_fill
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    widths = [22, 5, 7, 8, 52, 30, 18, 52, 12, 36, 6, 14, 44, 46]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        fill = PatternFill("solid", fgColor=pri_fill[row[2].value])
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
        row[2].fill = fill
    ws.freeze_panes = "E2"
    ws.auto_filter.ref = ws.dimensions

    s2 = wb.create_sheet("系列汇总")
    s2.append(["系列", "集数", "P1", "P2", "P3", "可量化关键词簇合计（US 月搜索量）"])
    for name in dict.fromkeys(r[0] for r in ROWS):
        rs = [r for r in ROWS if r[0] == name]
        tot = 0
        for r in rs:
            v = r[8].replace(",", "").replace("约", "").replace("+", "").split("（")[0].strip()
            tot += int(v) if v.isdigit() else 0
        s2.append([name, len(rs), sum(r[2] == "P1" for r in rs), sum(r[2] == "P2" for r in rs),
                   sum(r[2] == "P3" for r in rs), tot or "待补"])
    for c in s2[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head_fill
    for i, w in enumerate([28, 8, 6, 6, 6, 30], 1):
        s2.column_dimensions[get_column_letter(i)].width = w

    s3 = wb.create_sheet("说明")
    notes = [
        "数据来源：Semrush US broad-match 关键词库（cleaning / cutting / marking / welding，2026-11-08）、Semrush 自然排名导出、GSC 近 6 个月数据。",
        "已写清单：爬取 arcuscnc.com 全部 327 篇已发布文章（站点地图 220 篇 + 博客列表 107 篇）。每个选题都经过网址比对、关键词比对和站内搜索，确认没有专门文章。",
        "排除范围：已有文章的更新与合并（由你处理）；爱好者/CO2 非金属词（acrylic、wood、files、ideas）；顶漏斗定义词（what is / benefits / advantages）；城市本地词；竞品品牌词。",
        "S7 折弯机：上传的关键词表没有折弯机品类，目前只有 GSC 信号。建议补导出 'press brake' broad-match（US），再确定优先级和标题措辞。",
        "S5 单功率段文章：/laser-rust-removal-gun-wattage-guide/ 作为功率总览页，各功率段文章链接回总览页和价格枢纽页；单篇内不展开完整价格表，避免与价格页互相抢词。",
        "写作时按 arcuscnc_writing_rules_v3.md 执行：Pre-writing Brief、首段直接给答案、至少一个决策表、写明替代方案什么时候更好、FAQ 用真实搜索问句、列出 Items Pending Verification。",
    ]
    for n in notes:
        s3.append([n])
    s3.column_dimensions["A"].width = 140
    for row in s3.iter_rows():
        row[0].alignment = Alignment(wrap_text=True)
    wb.save(path)


def build_md(path):
    out = ["# arcuscnc.com 新选题规划：分系列、分集（2026-11-08）", "",
           "只列现有 327 篇已发布文章中没有专门覆盖的话题；已有文章的更新与合并不在本表范围内。",
           "表格版本见 `docs/arcuscnc-new-topic-series-2026-11.xlsx`（含筛选、系列汇总和说明三张表）。", ""]
    for name in dict.fromkeys(r[0] for r in ROWS):
        out += [f"## {name}", "",
                "| 集 | 优先级 | 周次 | 标题 | 核心关键词 | 量/KD | 簇总量 | URL | 类型 |",
                "|---|---|---|---|---|---|---|---|---|"]
        for r in [x for x in ROWS if x[0] == name]:
            out.append(f"| {r[1]} | {r[2]} | W{r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[8]} | `{r[9]}` | {r[11]} |")
        out.append("")
    out += ["## 说明", "",
            "- S7 折弯机缺少关键词库数据，建议补导出 press brake broad-match（US）后再定优先级。",
            "- S5 各功率段文章统一链接回功率总览页和价格枢纽页，单篇内不展开完整价格表。",
            "- 内链目标和防蚕食说明见 xlsx 的最后两列。", ""]
    open(path, "w").write("\n".join(out))


if __name__ == "__main__":
    build_xlsx("docs/arcuscnc-new-topic-series-2026-11.xlsx")
    build_md("docs/arcuscnc-new-topic-series-2026-11.md")
    print(len(ROWS), "topics")
