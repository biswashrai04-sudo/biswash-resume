import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace existing .chip CSS with glassmorphism version
old_chip = ".chip{background:var(--surface-2);border:1px solid var(--border);color:var(--muted);padding:8px 16px;border-radius:999px;font-size:.88rem;font-weight:500;transition:border-color .25s var(--ease),color .25s var(--ease),transform .25s var(--ease),background .25s var(--ease)}.chip:hover{border-color:var(--accent);color:var(--ink);transform:translateY(-2px);background:rgba(176,124,232,.06)}"

new_chip = """.chip{
  background:rgba(26,22,38,.55);
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
  border:1px solid rgba(176,124,232,.15);
  color:var(--muted);
  padding:8px 16px;border-radius:999px;font-size:.88rem;font-weight:500;
  box-shadow:0 0 8px rgba(176,124,232,.08),inset 0 0 8px rgba(176,124,232,.04);
  transition:border-color .3s var(--ease),color .3s var(--ease),transform .3s var(--ease),box-shadow .3s var(--ease);
}
.chip:hover{
  border-color:rgba(176,124,232,.45);
  color:var(--ink);
  transform:translateY(-2px);
  box-shadow:0 0 18px rgba(176,124,232,.25),inset 0 0 12px rgba(176,124,232,.08);
  background:rgba(26,22,38,.7);
}"""

html = html.replace(old_chip, new_chip)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Glass morphism applied")
