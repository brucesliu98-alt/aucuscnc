"""Classify GSC zero-click URLs (last 6 months) and assign a handling action.
Inputs: GSC export (网页 sheet), HTTP status file (url code redirect), crawled HTML dir,
sitemap URL lists. Output: docs/arcuscnc-zero-click-actions-2026-11.xlsx
"""
import os, re, sys, warnings
import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
warnings.filterwarnings('ignore')
S = sys.argv[1]
SITE = 'https://arcuscnc.com'
p = pd.read_excel('https___arcuscnc.com_-Performance-on-Search-2026-11-08.xlsx', sheet_name='网页')
p.columns = ['url', 'clk', 'imp', 'ctr', 'pos']
z = p[p.clk == 0].copy()
z['path'] = z.url.str.replace(SITE, '', regex=False)
st = {}
for l in open(f'{S}/zs.txt'):
    a = l.split(); st[a[0]] = (a[1], (a[2] if len(a) > 2 else '').replace(SITE, ''))
z['code'] = z.path.map(lambda x: st.get(x, ('?', ''))[0])
z['redirect_to'] = z.path.map(lambda x: st.get(x, ('', ''))[1])
sm = set(l.strip().replace(SITE, '') for f in ['post-sitemap1', 'post-sitemap2', 'page-sitemap', 'product-sitemap', 'service-sitemap', 'lq-project-sitemap'] for l in open(f'{S}/site/{f}.txt'))
z['in_sitemap'] = z.path.isin(sm).map({True: '是', False: '否'})

def pubdate(path):
    f = f"{S}/crawl/{path.lstrip('/').replace('/', '_')}.html"
    if not os.path.exists(f): return ''
    m = re.search(r'article:published_time" content="([0-9-]{10})', open(f, errors='ignore').read())
    return m.group(1) if m else ''
z['published'] = z.path.map(pubdate)

COPPER = {'/copper-melting-point-and-alloy-processing-tips/', '/melting-point-of-copper-directly-impacts-laser-welding/'}
BRASS = {'/brass-melting-temperature-inconsistent-across-alloys/'}
CORP = r'^/(gallery|industries|why-choose-us|get-in-touch|our-services|our-team|partners-clients|case-studies|products|about-us|contact-us)/$'
NOINDEX = r'^/(shop|cart|checkout|my-account|refund-policy|coming-soon|test11|download-2)/$'

def classify(r):
    u, code, imp, pos = r.path, r.code, r.imp, r.pos
    if code == '404':
        return ('A 站外错误网址（404）', '不处理', '保持 404。这些网址站内没有链接，多为外部采集站或 AI 内容写错的地址，展示极少，不影响排名。不要批量 301 到首页（会被判为软 404）。')
    if code == '301':
        return ('B 已跳转旧网址（301）', '不处理', f'跳转已生效（→ {r.redirect_to}）。GSC 会逐渐用目标网址替换；只需确认站内链接已改为目标网址。')
    if '/wp-content/' in u:
        return ('C 图片/附件文件', '不处理', '图片和 PDF 出现在网页搜索里属正常，零点击不影响站点。可确认 Rank Math 已开启"附件页跳转到父页面"。')
    if re.search(r'/page/\d+', u):
        return ('D 分页', '不处理', '分页保持 index, follow 即可，用于让 Google 发现深层文章；不要 noindex，也不要 301。')
    if re.search(r'^/(category|product-category)/', u):
        return ('E 分类归档', '低优先级优化', '保留。可在分类页顶部加 100–200 词介绍和精选文章，让它承接品类词；不要 noindex 博客/产品主分类。')
    if re.search(r'^/lq-project-category/', u):
        return ('E 分类归档', '设为 noindex', '行业项目分类页通常只有 1–2 个项目，内容很薄，建议 noindex, follow。')
    if re.search(NOINDEX, u):
        return ('F 功能/政策页', '设为 noindex', '购物车、结账、账户、政策、测试页不需要排名，建议 noindex；测试页（如 test11）直接删除。')
    if re.search(CORP, u):
        return ('F 公司介绍页', '不处理', '公司/联系类页面零点击属正常，用户多为直接访问或站内跳转。')
    if re.search(r'^/(product|service|lq-project)/', u):
        return ('G 产品/服务/行业页', '优化（不可删除或 noindex）', '询盘页面。改写 Title/Meta（写明功率、幅面、价格区间或"Get a quote"），补 Product Schema 与规格表，并从相关博客文章加 2–3 个内链。')
    if u in COPPER or u in BRASS:
        return ('H 同主题重复文章', '合并 + 301', '与同主题主文章（铜/黄铜熔点）重复，互相抢排名。合并有价值段落后 301 到主文章。')
    if imp >= 100 and pos <= 15:
        act = '改 Title/Meta 提高点击率'
        note = f'已有 {int(imp)} 次展示、排名 {pos:.1f}，问题在点击率。把核心答案写进 Title，Meta 写具体数字或对比结论。'
        if r.in_sitemap == '否': note += ' 同时补进站点地图。'
        return ('I 有展示、排名可见的文章', act, note)
    if imp >= 100:
        note = f'{int(imp)} 次展示但排名 {pos:.1f}，在第 2 页以后。补强内容（决策表、FAQ）并从高流量相关文章加内链。'
        if r.in_sitemap == '否': note += ' 同时补进站点地图。'
        return ('J 有展示、排名靠后的文章', '补强内容 + 内链', note)
    young = r.published and r.published >= '2026-05-09'
    if young:
        return ('K 新文章（发布不足 6 个月）', '观察，暂不处理', '发布时间短，零点击属正常。确保在站点地图中并有 2 个以上站内链接，3 个月后再评估。')
    return ('L 低展示老文章', '评估：补强 / 合并 / noindex', '发布已超过 6 个月仍展示很少。先查是否与其他文章主题重复（是则合并 301）；独立且对询盘有用的保留并补内链；都不是则 noindex。')

res = z.apply(classify, axis=1, result_type='expand'); res.columns = ['类别', '处理动作', '说明']
out = pd.concat([z[['url', 'imp', 'pos', 'code', 'redirect_to', 'in_sitemap', 'published']], res], axis=1)
out.columns = ['URL', '展示（6 个月）', '平均排名', 'HTTP 状态', '跳转到', '在站点地图中', '发布日期', '类别', '处理动作', '说明']
out = out.sort_values(['类别', '展示（6 个月）'], ascending=[True, False])
summ = out.groupby(['类别', '处理动作']).agg(网址数=('URL', 'count'), 展示合计=('展示（6 个月）', 'sum')).reset_index()

path = 'docs/arcuscnc-zero-click-actions-2026-11.xlsx'
with pd.ExcelWriter(path, engine='openpyxl') as w:
    summ.to_excel(w, sheet_name='汇总', index=False)
    out.to_excel(w, sheet_name='逐条处理清单', index=False)
    wb = w.book
    for ws, widths in [(wb['汇总'], [30, 30, 10, 12]), (wb['逐条处理清单'], [60, 12, 10, 10, 30, 12, 12, 28, 26, 80])]:
        for i, wd in enumerate(widths):
            ws.column_dimensions[chr(65 + i)].width = wd
        for c in ws[1]:
            c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor='1F3A5F')
        for row in ws.iter_rows(min_row=2):
            for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
        ws.freeze_panes = 'B2'; ws.auto_filter.ref = ws.dimensions
print(summ.to_string(index=False)); print(len(out))
