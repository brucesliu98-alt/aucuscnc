"""Convert an article .md (writing-rules v3 format) into:
  1. <slug>-wordpress.html : paste-ready HTML for the WordPress editor
     (no H1 - WordPress uses the post title; absolute internal links;
     FAQPage JSON-LD appended)
  2. <slug>-preview.html   : visual preview page with copy buttons

Usage: python3 articles/build_html.py articles/laser-cutting-software.md
"""
import html
import json
import re
import sys
from pathlib import Path

import markdown

SITE = "https://arcuscnc.com"


def meta_field(text, label):
    m = re.search(rf"\*\*{re.escape(label)}：\*\*\s*(.+)", text)
    if not m:
        return ""
    return re.sub(r"（\d+ 字符）$", "", m.group(1)).strip()


def main(md_path):
    src = Path(md_path)
    text = src.read_text(encoding="utf-8")
    seo_title = meta_field(text, "SEO Title")
    meta_desc = meta_field(text, "Meta Description")
    slug = re.search(r"\*\*Target URL:\*\*\s*/([^/\s]+)/", text).group(1)

    body = text.split("\n# ", 1)[1]
    body = "# " + body.split("\n---\n\n## Items Pending Verification")[0].strip()
    h1 = body.splitlines()[0][2:].strip()
    body_no_h1 = body.split("\n", 1)[1].strip()

    # absolute internal links
    body_no_h1 = re.sub(r"\]\((/[^)]+)\)", lambda m: f"]({SITE}{m.group(1)})", body_no_h1)

    content_html = markdown.markdown(body_no_h1, extensions=["tables"], output_format="html")
    content_html = content_html.replace("<table>", '<figure class="wp-block-table"><table>')
    content_html = content_html.replace("</table>", "</table></figure>")

    # FAQPage schema from the FAQ section
    faq_md = body_no_h1.split("## Frequently Asked Questions", 1)[1]
    faqs = []
    for q, a in re.findall(r"### (.+?)\n\n(.+?)(?=\n\n### |\Z)", faq_md, re.S):
        a_plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a.strip())
        a_plain = re.sub(r"\*\*|\*", "", a_plain)
        faqs.append({"@type": "Question", "name": q.strip(),
                     "acceptedAnswer": {"@type": "Answer", "text": a_plain}})
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faqs}
    schema_html = ('<script type="application/ld+json">\n'
                   + json.dumps(schema, ensure_ascii=False, indent=2)
                   + "\n</script>")

    wp_html = content_html + "\n\n" + schema_html + "\n"
    out_dir = src.parent
    wp_path = out_dir / f"{slug}-wordpress.html"
    wp_path.write_text(wp_html, encoding="utf-8")

    preview = PREVIEW.format(
        title=html.escape(seo_title),
        seo_title=html.escape(seo_title),
        seo_len=len(seo_title),
        meta_desc=html.escape(meta_desc),
        meta_len=len(meta_desc),
        slug=html.escape(slug),
        h1=html.escape(h1),
        content=content_html,
        code=html.escape(wp_html),
        faq_count=len(faqs),
    )
    prev_path = out_dir / f"{slug}-preview.html"
    prev_path.write_text(preview, encoding="utf-8")
    print(wp_path, prev_path, f"faqs={len(faqs)}", f"title={len(seo_title)}", f"meta={len(meta_desc)}")


PREVIEW = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{
  --bg: #f6f7f9; --card: #ffffff; --text: #1d2430; --muted: #5d6878;
  --line: #dde2e8; --accent: #1f5fae; --accent-soft: #e8f0fb; --code-bg: #0f1720; --code-text: #d7e1ee;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg: #11151b; --card: #1a2029; --text: #e6ebf2; --muted: #9aa6b5;
    --line: #2c3540; --accent: #6ea8ff; --accent-soft: #1c2a3d; --code-bg: #0b0f14; --code-text: #cfd9e6; }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.65 -apple-system, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif; }}
.wrap {{ max-width: 920px; margin: 0 auto; padding: 24px 16px 64px; }}
.panel {{ background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 20px; margin-bottom: 20px; }}
.panel h2.label {{ margin: 0 0 12px; font-size: 15px; color: var(--muted); font-weight: 600; letter-spacing: .02em; }}
.field {{ display: grid; grid-template-columns: 130px 1fr auto; gap: 10px; align-items: start; padding: 10px 0; border-top: 1px solid var(--line); }}
.field:first-of-type {{ border-top: 0; }}
.field .k {{ color: var(--muted); font-size: 14px; }}
.field .v {{ word-break: break-word; }}
.field .n {{ color: var(--muted); font-size: 12px; }}
button {{ font: inherit; font-size: 14px; border: 1px solid var(--accent); background: var(--accent); color: #fff;
  border-radius: 8px; padding: 6px 12px; cursor: pointer; white-space: nowrap; }}
button.ghost {{ background: transparent; color: var(--accent); }}
.toolbar {{ display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-bottom: 12px; }}
.toolbar .hint {{ color: var(--muted); font-size: 13px; }}
textarea {{ width: 100%; height: 260px; background: var(--code-bg); color: var(--code-text); border: 0; border-radius: 8px;
  padding: 12px; font: 12.5px/1.5 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; resize: vertical; }}
article h1 {{ font-size: 30px; line-height: 1.25; margin: 0 0 18px; }}
article h2 {{ font-size: 23px; margin: 36px 0 12px; padding-top: 8px; border-top: 1px solid var(--line); }}
article h3 {{ font-size: 18px; margin: 26px 0 8px; }}
article a {{ color: var(--accent); }}
article figure {{ margin: 18px 0; overflow-x: auto; }}
article table {{ border-collapse: collapse; width: 100%; font-size: 14.5px; min-width: 560px; }}
article th, article td {{ border: 1px solid var(--line); padding: 8px 10px; text-align: left; vertical-align: top; }}
article th {{ background: var(--accent-soft); }}
.toast {{ position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: var(--text); color: var(--bg);
  padding: 8px 14px; border-radius: 8px; font-size: 14px; opacity: 0; transition: opacity .2s; pointer-events: none; }}
.toast.show {{ opacity: 1; }}
@media (max-width: 600px) {{ .field {{ grid-template-columns: 1fr; }} article h1 {{ font-size: 24px; }} }}
</style>
</head>
<body>
<div class="wrap">

<section class="panel">
  <h2 class="label">SEO 设置（粘贴到 Rank Math / Yoast）</h2>
  <div class="field"><div class="k">SEO Title<div class="n">{seo_len} 字符</div></div><div class="v" id="f-title">{seo_title}</div><button class="ghost" data-copy="f-title">复制</button></div>
  <div class="field"><div class="k">Meta Description<div class="n">{meta_len} 字符</div></div><div class="v" id="f-meta">{meta_desc}</div><button class="ghost" data-copy="f-meta">复制</button></div>
  <div class="field"><div class="k">URL slug</div><div class="v" id="f-slug">{slug}</div><button class="ghost" data-copy="f-slug">复制</button></div>
  <div class="field"><div class="k">文章标题（H1）</div><div class="v" id="f-h1">{h1}</div><button class="ghost" data-copy="f-h1">复制</button></div>
</section>

<section class="panel">
  <h2 class="label">WordPress HTML 代码（正文 + FAQ Schema，共 {faq_count} 条 FAQ）</h2>
  <div class="toolbar">
    <button id="copy-code">一键复制 HTML</button>
    <span class="hint">古腾堡：添加"自定义 HTML"区块后粘贴，或在右上角"⋮ → 代码编辑器"中粘贴。经典编辑器：切换到"文本"标签后粘贴。</span>
  </div>
  <textarea id="code" readonly>{code}</textarea>
</section>

<section class="panel">
  <h2 class="label">可视化预览</h2>
  <article>
    <h1>{h1}</h1>
    {content}
  </article>
</section>

</div>
<div class="toast" id="toast">已复制</div>
<script>
function toast(msg) {{
  var t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show');
  setTimeout(function () {{ t.classList.remove('show'); }}, 1400);
}}
function copyText(text, el) {{
  if (navigator.clipboard && window.isSecureContext) {{
    navigator.clipboard.writeText(text).then(function () {{ toast('已复制'); }}, function () {{ fallback(el); }});
  }} else {{ fallback(el); }}
}}
function fallback(el) {{
  try {{
    if (el.select) {{ el.focus(); el.select(); }}
    else {{ var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }}
    document.execCommand('copy') ? toast('已复制') : toast('已选中，请按 Ctrl/Cmd + C');
  }} catch (e) {{ toast('已选中，请按 Ctrl/Cmd + C'); }}
}}
document.getElementById('copy-code').addEventListener('click', function () {{
  var c = document.getElementById('code'); copyText(c.value, c);
}});
document.querySelectorAll('[data-copy]').forEach(function (b) {{
  b.addEventListener('click', function () {{
    var el = document.getElementById(b.getAttribute('data-copy')); copyText(el.textContent.trim(), el);
  }});
}});
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main(sys.argv[1])
