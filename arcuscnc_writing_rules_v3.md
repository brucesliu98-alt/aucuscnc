# ArcusCNC 文章写作规则 v3
# 综合：结构指南 v2 + 实际写作模式（CT-01 / CL-01 / CL-02）
# 更新：2026-11-08

---

## 一、写前必做：Pre-writing Brief

每篇文章动笔前，先确认以下六项，全部回答后才开始写正文。

```
目标读者：[具体职位 / 行业 / 痛点场景，不能写"工厂采购"]
读者的核心问题：[从读者角度一句话描述，不是关键词]
文章直接答案：[包括适用条件和局限，能直接发给客户的结论]
防蚕食检查：[检查现有文章列表，确认没有已有文章覆盖同一意图]
漏斗位置：顶 / 中 / 底  → 中漏斗和底漏斗优先，AI会直接回答顶漏斗
待核实项：[写作前已知的信息缺口，列清楚]
```

---

## 二、关键词优先级

### ✅ 高优先级（写）
- **比较类**：laser vs plasma / pulsed vs CW / nitrogen vs oxygen
- **工况选型**：when to use / which process for / best for [material]
- **行业应用**：laser cleaning for [automotive / marine / battery]
- **故障排除**：not cutting through / error E04 / edge yellowing
- **价格/选购**：price / cost / how to choose / buyer's guide / manufacturer

### ⚠️ 降低优先级（AI正在商品化）
- What is laser cleaning / how does it work / basics / introduction
- 纯定义型文章（排名第一也不带流量）

---

## 三、文章开头规则

**第一段必须是核心答案，不是背景介绍。**

格式固定：
1. **直接给出结论**（含适用条件）
2. 本文覆盖的具体范围（工况/材料/功率段）
3. 什么情况下本文答案不适用

✅ 正确示例（CT-01开头）：
> Fiber laser cutting dominates 1–20 mm mild steel, stainless steel, and aluminum in job shops. Plasma cutting is more cost-effective per meter for carbon steel thicker than 25 mm at high volume. Waterjet cutting is the right answer when heat affects the material at any thickness.

❌ 禁止写法：
- "As technology continues to evolve…"
- "In this article, we will cover…"
- 先讲行业背景，第三段才给答案
- "This comprehensive guide…"

---

## 四、段落写法规则（AI 可见性核心）

每个 H3/H4 段落必须满足**自包含原则**：单独截取出来，不看上下文，仍能独立回答一个问题。

**结论前置**（先答后推）：

✅ 正确：
> Pulsed fiber lasers are the correct choice for paint, oxide, and rust removal on metal. The short pulse duration (10–500 ns) delivers enough peak power to ablate the contamination layer without raising the substrate surface above its melting point.

❌ 错误：
> Metal surfaces have different contamination types. Some contaminations are organic, some are inorganic. The laser interacts with the surface layer. Therefore, pulsed lasers are suitable for rust removal.

**长度控制**：每个语义块 150–300 词，不用一个 H3 统领 800 词的长论述。

**禁止引用上文**：不能写"如上所述"/ "as mentioned above" / "前文提到"。

---

## 五、文章结构模板

### 通用骨架

```
H1: [比较/判断型标题，直接回答核心问题]

[开头：核心答案 → 本文范围 → 局限说明]  约150词

H2: [第一个决策变量 / 对比维度]
  H3: [子选项A]
  H3: [子选项B]
  → 必须包含至少一个对比表格

H2: [成本/价格分析]
  → 必须包含价格范围表或计算示例
  → Hypothetical example 注明

H2: [应用/工况判断]
  → 实际场景，读者能直接对号入座

H2: [局限和诚实说明]
  → 写竞品/替代方案什么时候更好（建立信任）

H2: FAQ（5–7 条）
  → 每条 Q&A 自包含，Q 是实际搜索意图

[Delivery Summary] ← 仅在文件头部，不发布到网站
[Items Pending Verification]
```

### 文章类型对应结构重点

| 类型 | 核心结构重点 |
|------|-------------|
| 比较型（vs） | 统一评判标准 → 双向展示优劣 → 适用工况判断表 |
| 价格指南 | 分功率/规格的价格区间表 → 影响价格的关键因素 → TCO 计算 → ROI 场景 |
| 选购/厂商指南 | 评判标准定义 → 市场分层 → 关键规格解读 → 评估清单 |
| 行业应用 | 行业特有问题 → 工艺流程 → 验证要求 → 局限说明 |
| 故障排除 | 症状 → 机制 → 解法 → 预防措施 |

---

## 六、表格写法规则

**每篇文章至少一个核心决策表格**，读者能直接查表做判断。

表格要求：
- 表头描述维度，不用模糊词（✅ "功率段 / 材料" ❌ "参数"）
- 每个单元格给具体值或明确判断（✅ "USD 60K–90K" ❌ "较低"）
- 表格下方必须有一行"How to read the table:"解释适用条件
- 超过 5 行的表格加粗最推荐选项

示例（来自 CL-01）：
```
| 功率段 | 价格区间（人民币）| 推荐场景 |
|--------|-----------------|---------|
| 100W pulsed | ¥80K–120K | 精密零件表面清洁，涂层去除 |
| 500W pulsed | ¥150K–250K | 中型制造业，汽车零部件 |
...
```

---

## 七、数字和数据规则

### 允许
- 有据可查的行业通行数据（ISO 标准、公开规格）
- 价格区间（注明"as of 2026, CNY/USD"）
- 计算示例（必须标注 `Hypothetical example:`）
- 物理参数（波长、频率、功率密度）

### 禁止
- 编造测试数据（"经我们测试，效率提升 40%"）
- 编造案例引用（虚构客户名、地区）
- 编造证书/认证（"通过 XYZ 认证"）
- 市场数据不注明时间和来源

### 不确定时的写法
> "Typical range based on published manufacturer specs; actual values depend on material, contamination type, and line configuration. Verify with your supplier before budgeting."

---

## 八、诚实局限原则

**每篇文章必须写竞品/替代方案什么时候更好。** 不写局限 = 不可信。

示例（来自 CT-01）：
> **When plasma wins:** Carbon steel above 25 mm at high volume. Plasma delivers a lower cost per metre than any laser system at this thickness range.
> 
> **When waterjet is the only answer:** Heat-sensitive materials — composites, hardened tool steel, stone, glass. No laser or plasma process is acceptable here.

---

## 九、FAQ 写法规则

- 5–7 条，每条 Q&A 自包含（不引用正文）
- Q 必须是真实搜索意图（从 GSC 数据提取，不是自己想的）
- A 长度：50–120 词，给具体答案，不引导到正文

✅ 好的 FAQ Q：
- "What is the difference between pulsed and continuous-wave laser cleaning?"
- "Is a 1000W laser cleaner enough for automotive rust removal?"

❌ 差的 FAQ Q：
- "What are the advantages of laser cleaning?"（顶漏斗，AI 直接回答）
- "Why choose ArcusCNC?"（推销感太强）

---

## 十、文章元信息（文件头部必填）

每篇文章 .md 文件顶部写：

```markdown
**Target keyword:** [主关键词] / [次要关键词]
**Target URL:** /slug/（注明：是新建页面还是替换现有页面）
**Content type:** [漏斗位置] · [文章类型] · [约 X 词]
**Reviewed:** [YYYY-MM]
**Status:** 待发布 / 已发布 / 需301合并
**301 source:** （如有）原URL → 新URL
```

---

## 十一、关键词分布与语义覆盖规则

Google 不要求特定密度百分比，但关键词在页面中的**位置**和**变体覆盖**直接影响相关性判断。

### 核心关键词分布（位置优先于密度）

| 位置 | 要求 | 示例 |
|------|------|------|
| SEO Title | 必须包含，尽量靠前 | "Laser Cleaning Machine Price: 500W to 3000W Cost Guide" |
| Meta Description | 必须包含，自然融入 | "…laser cleaning machine price ranges from ¥80K to ¥800K depending on power…" |
| H1 | 必须包含，可以是变体形式 | H1 与 Title 可以不同，但核心词要在 |
| 正文前 100 词 | 必须出现至少 1 次 | 开头段直接回答问题，关键词自然出现 |
| 至少 1 个 H2 | 建议包含，可用变体 | "Laser Cleaning Machine Cost by Power Tier" |
| 正文中 | 自然出现，不强制次数 | 读起来像正常句子，不像关键词堆砌 |
| Alt text（如有图片）| 描述图片内容，可包含关键词 | "500W pulsed fiber laser cleaning machine" |

**核心原则：关键词在正确位置出现一次，比在错误位置出现十次更有效。**

### 语义覆盖（LSI 词 / 相关变体）

Google 判断页面相关性，不只看主关键词，还看页面是否覆盖了该话题应该讨论的相关词汇。写文章时，以下变体词应自然出现在正文中：

**方法：写完正文后，对照下方逻辑检查是否覆盖**

1. **主关键词的同义/变体形式**
   - 主词：laser cleaning machine price
   - 变体：laser cleaner cost / cleaning laser price / fiber laser cleaning machine price / laser rust removal machine price

2. **话题应该提到的相关概念**（读者期待看到的词，不出现会显得内容浅薄）
   - 价格类文章：power tier / pulsed vs CW / TCO / ROI / warranty / consumables cost
   - 比较类文章：HAZ / kerf width / assist gas / operating cost / material thickness
   - 厂商类文章：fiber laser source / galvo scanner / cooling system / CE certification / IP rating

3. **用户在同一话题下会搜索的问题词**（放进 H2/H3 或 FAQ）
   - "how much does a laser cleaning machine cost"
   - "laser cleaning machine price vs sandblasting"
   - "is 1000W laser cleaner enough"

### 语义覆盖检查清单（写完后对照）

```
□ 主关键词出现在 H1、前100词、至少1个H2
□ Meta Description 自然包含主关键词
□ 正文包含 3–5 个语义相关变体词
□ 文章覆盖了该话题"应该讨论"的核心概念（不出现会让读者觉得内容不完整）
□ FAQ 中至少 2 条 Q 包含用户实际搜索的长尾变体
□ 没有连续两句话使用完全相同的关键词短语（避免堆砌感）
```

### 禁止做法

- 在一个段落内重复同一关键词短语 3 次以上
- 为了密度在句末强行加"laser cleaning machine"
- 把关键词塞进不相关的句子（"As a laser cleaning machine price leader…"）
- H2 全部都是关键词变体，没有实际内容价值

---

## 十二、内部链接规则

- 链接写在正文段落中，自然出现，不单独放"Related articles"区块
- Anchor text 描述目标内容，不重复同一主关键词
- 同一目标 URL 在同一文章最多出现 2 次
- 不写"See also"段落（为链接而写的假内容）

---

## 十三、常青化规则（Evergreen）

适用于"Best / Top 5"类文章：

- 标题去掉年份（❌ "Top 5 Laser Cleaning Machines 2026" → ✅ "Best Industrial Laser Cleaning Machines"）
- URL 去掉年份
- 文中加 "Updated Annually" 标注
- 不点名竞品排名（改为：评判框架 + 读者自查清单）
- 不写"As of this writing"（会立刻过期）

---

## 十四、Delivery Summary 格式

每篇文章交付时，在文件头部附：

```
## Delivery Summary
- 文章定位：[与现有文章的差异，一句话]
- SEO Title：[≤60字符]
- H1：[与 SEO Title 可以不同，更口语化]
- Meta Description：[≤155字符，含主关键词，含价值主张]
- 漏斗位置：[顶/中/底]，AI直接回答该查询的概率：[低/中/高]
- 推荐 Schema：[FAQPage / HowTo / Article / Product]
- 内部链接建议：
  - [锚文本] → [目标URL]
- 301 建议：（如有）
```

---

## 十五、Items Pending Verification

每篇文章结尾列出未核实项，格式：

```
## Items Pending Verification
1. [具体 claim] — 来源建议：[官网/标准文件/供应商报价]
2. ...

如核实项 > 3 条且涉及文章核心结论，注明：⚠ 建议发布前完成核实。
```

不能写"数据待确认"这种模糊表述，必须说清楚具体是哪句话。

---

## 十六、禁止事项（快查清单）

| 禁止 | 原因 |
|------|------|
| 编造案例、引用、证书 | E-E-A-T 违规，法律风险 |
| 绝对表述（zero damage / completely safe / suitable for all） | 不诚实，容易被攻击 |
| 标题承诺 > 文章交付 | 跳出率高，信任损失 |
| 只改发布日期不更新内容 | Google 明确打击（GEO Spam） |
| 一篇文章多次对同一URL做内部链接（>2次） | 锚文本稀释 |
| 段落引用上文（"如上所述"） | AI 无法摘取该段落 |
| 推销型自夸（"ArcusCNC 是最好的"） | 买家不信，直接关闭 |
| 编造竞品参数做对比 | 法律风险 |

---

*本规则基于：结构指南 v2（2026-10-14）+ CT-01 / CL-01 / CL-02 实际写作模式（2026-11）*
