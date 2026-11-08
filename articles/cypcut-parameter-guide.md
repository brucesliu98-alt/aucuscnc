**Target keyword:** cypcut parameters / cypcut; cypcut flycut
**Target URL:** /cypcut-parameter-guide/ (new page)
**Content type:** Middle of funnel · Tutorial + troubleshooting (教程 / 故障) · ~3,500 words
**Reviewed:** 2026-11
**Status:** 待发布
**301 source:** None

## Delivery Summary
- **文章定位：** 全站第一篇系统讲 CypCut 参数结构（全局 / 图层 / 图形工艺三级）、分段穿孔填写、引线与补偿、工艺库管理的文章。/fly-cutting/ 和 /frog-jump-cutting/ 已有 CypCut 设置步骤，本文只做一节衔接并链接过去，避免抢 "cypcut flycut" 一词；穿孔原理和焦点原理同样只链接到现有文章。
- **SEO Title：** CypCut Parameters: Layers, Piercing, Lead-ins & Libraries
- **H1：** CypCut Parameter Setup: Layers, Piercing, Lead-ins and Cutting Process Libraries
- **Meta Description：** How CypCut parameters are organized and set: layer settings, multi-stage piercing, lead-ins, kerf compensation and a reusable process library.
- **漏斗位置：** 中（已购机用户 + 正在比较控制系统的买家）。AI 直接回答该查询的概率：低–中（AI 很难给出按 CypCut 结构组织的设置顺序和故障对照）。
- **推荐 Schema：** Article + FAQPage（如需可加 HowTo，对应"参数设置顺序"一节）
- **内部链接建议：**
  - laser cutting software layers → /laser-cutting-software/（S1-1，需先发布）
  - assist gas selection → /assist-gas-selection-laser-cutting-guide/
  - focus position → /setting-the-laser-focus-position/
  - multi-stage piercing for thick plate → /optimizing-laser-piercing-parameters-for-thick-plate-cutting/
  - burr-free piercing on stainless → /burr-free-laser-piercing-stainless/
  - fly cutting setup → /fly-cutting/
  - frog jump → /frog-jump-cutting/
  - capacitive sensor / BCS100 calibration → /troubleshooting-capacitive-sensor-errors/
  - stainless steel cutting speed chart → /laser-cutting-machine-stainless-steel-speed/
- **301 建议：** 无

---

# CypCut Parameter Setup: Layers, Piercing, Lead-ins and Cutting Process Libraries

CypCut parameters are organized in three levels: **global parameters** set machine-wide motion behavior, **layer parameters** hold the complete cutting process for every contour drawn in that layer color, and **graphic process settings** such as lead-ins, kerf compensation and micro-joints are attached to individual parts in the drawing. Most cut-quality problems are solved in the layer parameters, most edge-mark and dimension problems are solved in the graphic process settings, and most cycle-time problems are solved in the global parameters. The fastest way to stable results is to tune in a fixed order (height and focus, then gas, then speed and power, then piercing, then lead-ins) and save each proven combination of material, thickness, gas and nozzle in a process library so operators load it instead of retyping it.

This guide applies to CypCut 2D sheet cutting on Friendess (BOCHU) FSCUT control systems with a BCS100 capacitive height controller. Menu names and the exact list of fields differ between CypCut versions, and HypCut (high-power) and tube cutting software use different screens, so treat the field names here as a map and confirm them in your version's manual.

## How CypCut Parameters Are Organized

CypCut separates settings by how often they change. Knowing which level a setting lives on stops the most common mistake: changing a machine-wide value to fix one part.

| Level | Where it is set | What it controls | How often it changes |
|---|---|---|---|
| Global parameters | Global or machine parameter settings | Travel speed and acceleration between contours, lift mode (normal lift or leapfrog), return position, edge seeking behavior | Rarely; after machine commissioning or a motion upgrade |
| Layer parameters | Layer (process) parameter dialog, one tab per layer color | Cutting speed, laser power, frequency, duty cycle, gas type and pressure, cutting height, focus, piercing stages, slow start, laser-off delay | Every time material, thickness, gas or nozzle changes |
| Graphic process settings | Applied to selected parts in the drawing | Lead-in and lead-out, kerf compensation, micro-joints, cutting sequence, start points, cooling points, FlyCut grouping | Every new job |

**How to read the table:** if a problem appears on every part of one material, change the layer parameters. If it appears only at the start or end of a contour, change the graphic process settings. If it only costs time, look at the global parameters.

For how CypCut fits alongside CAD and nesting software, see our overview of the [three layers of laser cutting software](/laser-cutting-software/).

## Layer Parameters: What Each Setting Controls

Each CypCut layer stores a full cutting recipe. Every contour drawn in that layer color is cut with that recipe, so layers are also the tool for giving different features of the same part different settings.

### The Core Cutting Settings

The table below lists the layer parameters that decide edge quality, what each one controls, and which direction to adjust it.

| Layer parameter | What it controls | Raise it when | Lower it when |
|---|---|---|---|
| Cutting speed | Energy per millimeter of cut | Edge shows burn marks, wide kerf, or heavy oxidation | Cut does not go through, sparks spray upward, dross hangs at the bottom |
| Peak power (%) | Laser output during cutting | Cut fails to penetrate at the target speed | Kerf is wide or the top edge melts on thin sheet |
| Frequency and duty cycle | Pulse behavior; continuous wave at 100% duty | Use continuous wave for straight cutting on most sheet | Use pulsed output for small holes, sharp corners and fine features to reduce overheating |
| Gas type | Cutting chemistry: oxygen burns, nitrogen and air melt | Switch to nitrogen when an oxide-free edge is required | Switch to oxygen for thick mild steel where speed per kW matters more than edge color |
| Gas pressure | Melt ejection | Dross sticks to the bottom edge | Edge is rough from turbulence or gas use is excessive |
| Cutting height | Nozzle-to-sheet standoff held by the BCS100 | Spatter reaches the nozzle or the head touches tipped parts | Gas flow is not reaching the kerf and dross increases |
| Focus position | Where the beam waist sits relative to the sheet | Moving focus deeper helps thick nitrogen cuts | Moving focus upward helps thin sheet and oxygen cutting |

**How to read the table:** change one parameter at a time and cut a short test line after each change. Changing speed and pressure together hides which one fixed the problem. Gas choice is explained in our [assist gas selection guide](/assist-gas-selection-laser-cutting-guide/), and focus behavior is explained in our guide to [setting the laser focus position](/setting-the-laser-focus-position/).

Published speed and power figures are a starting point, not a final value. Laser source brand, cutting head optics, nozzle size and gas purity all move the working window, so a value copied from another machine usually needs adjustment. For stainless steel starting speeds by thickness, use our [stainless steel cutting speed chart](/laser-cutting-machine-stainless-steel-speed/).

### Start and End Settings Inside the Layer

Three layer settings control what happens at the beginning and end of each contour, where most visible defects start.

- **Slow start (slow lead-in):** the cutting head runs at reduced speed for a short distance after piercing, so the cut stabilizes before reaching full speed. It prevents a burned or unseparated section right after the pierce point. Increase the slow-start distance on thick plate and on oxygen cutting.
- **Laser-off delay:** keeps the beam on briefly at the end of a contour so the last millimeter separates fully. Too long a delay leaves a burn mark at the closing point.
- **Corner and speed-related power control:** reduces power automatically when the head slows down at corners, preventing burned corners on thin sheet. If corners burn while straight edges are clean, check this setting before lowering power for the whole layer.

### Planning Layers for One Part

Assigning features to separate layers lets one part be cut with several recipes. A typical layer plan for a sheet metal part looks like this:

| Layer use | Typical difference from the main contour layer | Why |
|---|---|---|
| Main outer contours | Reference recipe for the material and thickness | Highest edge-quality priority |
| Small holes (diameter close to sheet thickness) | Lower speed, pulsed output, shorter lead-in | Prevents oval or burned holes |
| Fine slots and text cut through | Pulsed output, reduced power | Limits heat build-up in narrow features |
| Surface marking or scoring lines | Low power, no piercing, cut does not penetrate | Bend lines or part numbers without separate marking equipment |
| Do-not-cut reference geometry | Layer disabled for output | Keeps reference lines in the file without cutting them |

**How to read the table:** start with one layer per material and thickness and add feature layers only when a specific feature fails with the main recipe. Every extra layer is another recipe to maintain in the process library.

## Piercing Setup in CypCut

Piercing parameters sit inside each layer and run before the cutting recipe starts. The piercing mode decides how many stages the pierce uses, and each stage has its own height, power, frequency, duty cycle, gas, pressure, focus and dwell time.

### Choosing the Piercing Mode

| Material thickness (mild steel, oxygen) | Recommended piercing mode | Reason |
|---|---|---|
| Up to about 3 mm | No separate pierce, or a short single-stage pierce | The cut parameters penetrate almost instantly |
| About 4–10 mm | Single-stage pulsed pierce | Controlled pulses open the hole without blowing molten metal back at the nozzle |
| **About 12 mm and above** | **Two- or three-stage progressive pierce** | **Starts high with low duty cycle, then steps closer and stronger, protecting the protective lens from spatter** |
| Thick plate in long production runs | Multi-stage pierce plus pre-piercing | All holes are pierced first, then cut, so heat from piercing does not affect cutting |

**How to read the table:** thickness bands shift with laser power. A higher-power source moves each band toward thicker material; stainless and aluminum with nitrogen usually need more conservative piercing than mild steel of the same thickness. Treat these bands as typical starting points and confirm them with a test pierce on your material.

In a multi-stage pierce, the first stage normally uses a higher nozzle height, lower duty cycle and lower power to start the hole without heavy back-spatter. Later stages move closer, raise duty cycle and power, and finish the hole. A short dwell between the last stage and the cut start prevents the cut from beginning in an incompletely opened hole.

The physics behind frequency, duty cycle and pierce focus is covered in our guide to [multi-stage piercing for thick plate](/optimizing-laser-piercing-parameters-for-thick-plate-cutting/). Stainless steel users who see a raised burr around the pierce point should read our guide to [burr-free piercing on stainless steel](/burr-free-laser-piercing-stainless/).

### Pre-Piercing and Cooling Points

Pre-piercing pierces every contour on the sheet first and then cuts them in sequence. It reduces the risk that a hot, just-cut area affects the next pierce, and it is most useful on thick mild steel. Cooling points pause the beam at a selected position, typically at a sharp corner on thick plate, so heat dissipates before the head continues. Both add cycle time, so apply them only to the material and thickness ranges that need them.

## Lead-ins, Lead-outs and Kerf Compensation

Lead-ins, lead-outs and compensation are graphic process settings, not layer settings. They are applied to selected parts and decide where each contour starts, where it ends, and whether the finished part matches the drawing dimensions.

### Lead-in and Lead-out Rules

The lead-in moves the pierce point off the finished edge so the pierce mark lands in scrap. The lead-out carries the cut past the closing point so the part separates cleanly.

| Feature | Lead-in type | Lead-in position | Reason |
|---|---|---|---|
| Outer contour | Straight line or line plus arc | On a corner or a straight edge on the scrap side | Pierce mark falls outside the part; corner starts hide the closing mark |
| **Inner hole, medium to large** | **Arc lead-in from the hole center side** | **On a straight section or the longest arc** | **Arc entry avoids a notch where the lead meets the contour** |
| Small hole (close to sheet thickness) | Short straight lead-in from near the center | Center area of the hole | Lead-in must fit inside the hole without crossing the edge |
| Visible cosmetic edge | Lead-in placed on a hidden edge | Edge that will be bent, welded or covered | Keeps the start and end marks off visible surfaces |
| Thick plate | Longer lead-in | Away from sharp corners | Gives the pierce and slow start room to stabilize before the edge |

**How to read the table:** the lead-in must always start on the scrap side of the contour, outside an outer contour and inside a hole. A lead-in that is too long on small holes cuts into the part edge; a lead-in that is too short on thick plate puts the pierce crater on the finished edge.

Overcut or a small seal gap at the closing point controls how the contour ends. A slight overcut guarantees separation; a seal gap leaves a tiny uncut section that acts as a micro-joint. Excess overcut leaves a visible notch where the cut passes the start point.

### Kerf Compensation

The laser removes a strip of material equal to the kerf width, so an uncompensated outer contour comes out undersized and an uncompensated hole comes out oversized. Kerf compensation offsets the cutting path by half the kerf width: outward for outer contours and inward for holes.

Measure the kerf on a test cut for each material, thickness and nozzle combination, and store the compensation value together with that recipe. Kerf width changes with focus position, nozzle size and gas pressure, so a compensation value that was correct before a nozzle change may no longer be correct after it.

### Micro-joints and Cutting Sequence

Micro-joints are short uncut sections that hold small parts in the skeleton so they cannot tip up into the head path. Use them on parts small enough to fall through or rotate between support slats. Cut inner contours before outer contours, and cut small parts before large ones, so each part stays supported by the sheet until its last contour is finished.

## FlyCut and Leapfrog: Motion Settings That Depend on Your Layers

CypCut FlyCut cuts rows of identical small shapes, such as grids of round or square holes, in a continuous motion without stopping and lifting between shapes. Leapfrog (frog jump) shortens travel between contours by lifting and moving the head along an arc instead of up, across and down.

Both functions change motion, not the cutting recipe, but they only work with suitable layer settings. FlyCut needs a pierce that is fast enough to happen on the move, which in practice limits it to thin sheet with short or no piercing, and it raises the risk of tipped parts because the head does not lift between shapes. Leapfrog lifts the head less than a normal lift, so micro-joints and a correct cutting sequence become more important to avoid collisions.

The full FlyCut setup steps and risks are in our guide to [fly cutting](/fly-cutting/), and leapfrog settings are covered in our guide to [frog jump cutting](/frog-jump-cutting/).

## Building a Reusable Process Library

A process library stores proven layer parameters so the same material, thickness, gas and nozzle always load the same recipe. Without a library, each operator rebuilds parameters from memory and cut quality varies between shifts.

### What to Store for Each Recipe

Each entry should capture everything that changes the result, not only speed and power. A recipe without the nozzle size and focus value cannot be reproduced.

| Field | Example entry |
|---|---|
| Material and grade | Stainless 304 |
| Thickness | 3 mm |
| Gas and purity | Nitrogen, 99.99% |
| Nozzle type and diameter | Single-layer, 2.0 mm |
| Laser source power | 6 kW |
| Layer recipe | Speed, power, frequency, duty cycle, pressure, height, focus |
| Piercing stages | Mode and values for each stage |
| Kerf compensation | Measured value for this recipe |
| Date, operator and test result | Date tested, who tested, edge quality notes |

**How to read the table:** the example values show the format, not recommended settings. A consistent naming pattern such as material_thickness_gas_nozzle (for example SS304_3mm_N2_D2.0) lets operators find the right recipe without opening each one.

### Library Management Practices

- **Test before saving:** cut a test coupon with straight edges, a small hole and a sharp corner, and save the recipe only after all three pass inspection.
- **Restrict editing:** let operators load recipes and let only the process owner overwrite them, so a temporary adjustment does not become the new standard.
- **Record changes:** note the date and reason whenever a recipe changes, such as a new gas supplier or a nozzle type change.
- **Back up the library:** export the parameter files to a separate drive regularly and before any software update or industrial PC replacement.
- **Re-validate after hardware changes:** a new protective lens, nozzle type, laser source or cutting head can shift the working window, so re-test the most-used recipes after any of these changes.

## Tuning Order and Troubleshooting Table

Tuning in a fixed order prevents chasing one problem with the wrong parameter. Confirm the hardware first: clean protective lens, centered nozzle, calibrated BCS100 height controller and correct gas purity. Then tune in this order: cutting height and focus, gas type and pressure, speed and power, piercing, slow start, and finally lead-ins and compensation.

| Symptom | Check first | Check next |
|---|---|---|
| Dross on the bottom edge | Gas pressure, focus position | Cutting speed |
| Cut does not go through | Cutting speed, focus position | Power, protective lens condition |
| Burn mark or unseparated section right after the pierce | Slow start distance and speed | Pierce dwell time |
| Pierce blowout or spatter on the nozzle | Number of pierce stages, first-stage height | First-stage duty cycle and power |
| Burned corners on thin sheet | Corner power control | Pulsed output for the corner-heavy layer |
| Oval or burned small holes | Separate small-hole layer with lower speed | Lead-in length, pulsed output |
| Notch where the contour closes | Overcut length, lead-in type | Laser-off delay |
| Parts undersized or holes oversized | Kerf compensation direction and value | Focus and nozzle changes since the last measurement |
| Head collides with tipped parts | Micro-joints, cutting sequence | Lift mode (leapfrog) and FlyCut use |
| Height alarms or unstable standoff | BCS100 calibration, nozzle and ceramic ring | Grounding and cable connections |

**How to read the table:** work through the first column before touching the second. If a symptom appears suddenly on a recipe that worked before, suspect hardware (lens, nozzle, gas) before changing parameters. Height-control alarms are covered in our guide to [capacitive sensor errors](/troubleshooting-capacitive-sensor-errors/).

## Limitations of Parameter Tuning

CypCut parameters can only control what the hardware allows. Several common problems cannot be fixed in software.

**When the hardware is the cause:** a contaminated protective lens, an off-center nozzle, a damaged ceramic ring or low gas purity produce the same symptoms as bad parameters. Adjusting parameters to compensate for worn hardware creates recipes that fail as soon as the part is replaced.

**When parameters from another machine do not transfer:** recipes depend on the laser source, cutting head optics, nozzle and gas supply. A parameter file from another machine, even another CypCut machine, is a starting point that needs re-testing, not a finished recipe.

**When a different software screen applies:** HypCut on high-power machines and tube cutting software organize parameters differently, and some fields described here may be named or grouped differently in your CypCut version.

**When the material is the limit:** highly reflective metals, heavily rusted or painted plate, and coated sheet can fall outside a stable working window regardless of parameters. Material preparation or a different process may be the better answer.

## Frequently Asked Questions

### What are the most important CypCut parameters to set first?

Set cutting height and focus position first, then gas type and pressure, then cutting speed and power. These parameters decide whether the cut penetrates and how much dross remains. Piercing, slow start, lead-ins and kerf compensation come next, because they only affect the start, end and dimensions of each contour. Changing one parameter at a time and cutting a short test line after each change makes it clear which setting fixed the problem.

### How do I save and reuse cutting parameters in CypCut?

CypCut stores cutting parameters per layer, and proven layer parameters can be saved to a material or process library and loaded for later jobs. Save each recipe under a name that includes material, thickness, gas and nozzle, for example SS304_3mm_N2_D2.0, so operators can find it quickly. Export the library to a backup drive before software updates or industrial PC replacement, and re-test saved recipes after any change of nozzle, lens or laser source.

### Can I copy CypCut parameters from another machine?

You can import parameters from another machine, but treat them as a starting point. Cutting results depend on the laser source, cutting head optics, nozzle type, gas purity and pressure delivery, and these differ between machines even when both run CypCut. Cut a test coupon with a straight edge, a small hole and a corner, adjust focus, pressure and speed as needed, and save the adjusted recipe as a new entry.

### What is slow start in CypCut?

Slow start is a layer setting that runs the cutting head at reduced speed for a short distance after the pierce, before accelerating to full cutting speed. It lets the cut stabilize so the first section of the contour separates cleanly instead of showing burn marks or an uncut section. Thick plate and oxygen cutting usually need a longer slow-start distance than thin sheet cut with nitrogen.

### How do I set lead-ins for small holes in CypCut?

Use a short straight lead-in starting near the center of the hole, so the lead-in fits inside the hole without crossing its edge. For holes with a diameter close to the sheet thickness, place them on a separate layer with lower speed and pulsed output, because the main contour recipe usually overheats small features. Check the finished hole for roundness and a notch at the closing point, and adjust overcut if needed.

### What is CypCut FlyCut and when should I use it?

CypCut FlyCut cuts rows of identical small shapes, such as grids of holes in perforated panels, in a continuous motion without stopping or lifting between shapes. It can greatly reduce cycle time on thin sheet, but it needs fast or no piercing and raises the risk of tipped parts and slightly oval holes at high speed. It is best suited to thin sheet with regular hole patterns and is not suited to thick plate.

### Why does the pierce point burn or blow out in CypCut?

A burned or blown-out pierce usually means the piercing recipe delivers too much energy too early or too close to the sheet. Add a piercing stage, start the first stage at a higher nozzle height with lower duty cycle and power, and add a short dwell before the cut begins. If the problem started suddenly on a recipe that previously worked, check the protective lens, nozzle and gas pressure before changing parameters.

---

## Items Pending Verification
1. 三级参数结构及菜单名称（Global parameters / Layer parameters / 图形工艺设置）在当前 CypCut 版本中的实际叫法与位置 — 来源建议：Friendess CypCut 用户手册（与 ArcusCNC 出厂版本一致的版本号）。
2. "Corner and speed-related power control" 在 CypCut 中的具体功能名称（如功率曲线/频率曲线）— 来源建议：CypCut 用户手册"图层参数"章节。
3. 穿孔方式厚度分段（≤3 mm 不单独穿孔；4–10 mm 单段脉冲；≥12 mm 两到三段渐进穿孔）— 来源建议：ArcusCNC 应用工程师按 3 kW / 6 kW / 12 kW 机型确认，必要时按功率分列。
4. Material library（材料库 / 工艺库）的保存、导入导出方式及文件格式 — 来源建议：CypCut 用户手册；如版本不支持导出，删除"Export the library"相关句子。
5. 编辑权限限制（只允许工艺负责人覆盖配方）在 CypCut 中是否有权限设置功能，还是需要靠管理制度执行 — 来源建议：CypCut 用户手册或 Friendess 技术支持。
6. FlyCut 的适用条件（薄板、无穿孔或快速穿孔、规则图形）— 来源建议：CypCut FlyCut 功能说明，并与 /fly-cutting/ 现有内容保持一致。
7. 工艺库示例表中的值（SS304、3 mm、N2 99.99%、2.0 mm 单层喷嘴、6 kW）仅作格式示例，已在表下注明；发布前确认不会被读者理解为推荐参数。

⚠ 核实项超过 3 条，且第 1、3 条涉及文章核心结构和参数建议，建议发布前请应用工程师或 Friendess 文档完成核实。
