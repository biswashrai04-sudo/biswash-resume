import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Add framed job CSS
frame_css = """
/* -------- EXPERIENCE FRAMES -------- */
.job{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);padding:24px 28px;margin-bottom:16px;transition:border-color .3s var(--ease),transform .3s var(--ease)}
.job:hover{border-color:rgba(176,124,232,.35);transform:translateY(-2px)}
.job::before{content:"";position:absolute;left:0;top:0;height:2px;width:0;background:linear-gradient(90deg,var(--primary),var(--accent));border-radius:var(--radius-md) var(--radius-md) 0 0;transition:width .35s var(--ease)}
.job:hover::before{width:100%}
.job{position:relative;overflow:hidden;border-top:none}
.job:first-child{border-top:1px solid var(--border)}
"""
html = html.replace("</style>", frame_css + "\n</style>")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Frame added")
