import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Find exact chip CSS and replace
chip_start = html.index('.chip{background:var(--surface-2)')
chip_end = html.index('.chip:hover{border-color:var(--accent)') 
chip_end = html.index('}', chip_end) + 1

old_chip = html[chip_start:chip_end]

new_chip = """.chip{
  background:rgba(26,22,38,.55)!important;
  backdrop-filter:blur(14px)!important;
  -webkit-backdrop-filter:blur(14px)!important;
  border:1px solid rgba(176,124,232,.18)!important;
  color:var(--muted);
  padding:8px 16px;border-radius:999px;font-size:.88rem;font-weight:500;
  box-shadow:0 0 10px rgba(176,124,232,.1),inset 0 0 8px rgba(176,124,232,.05);
  transition:border-color .3s var(--ease),color .3s var(--ease),transform .3s var(--ease),box-shadow .3s var(--ease)!important;
}
.chip:hover{
  border-color:rgba(176,124,232,.5)!important;
  color:var(--ink)!important;
  transform:translateY(-2px)!important;
  box-shadow:0 0 20px rgba(176,124,232,.3),inset 0 0 12px rgba(176,124,232,.08)!important;
  background:rgba(26,22,38,.7)!important;
}"""

html = html[:chip_start] + new_chip + html[chip_end:]

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Chip glass applied")
