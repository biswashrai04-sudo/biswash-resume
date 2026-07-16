import os, re
path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove photo-frame div from hero
html = re.sub(r'<div class="photo-frame reveal">\s*<img src="profile\.png"[^/]*/>\s*</div>', '', html)

# Remove photo-frame CSS (from .photo-frame to the closing } of each block)
# Remove @keyframes float
html = re.sub(r'@keyframes float\{.*?\n\}', '', html, flags=re.DOTALL)
# Remove @keyframes shadowPulse
html = re.sub(r'@keyframes shadowPulse\{.*?\n\}', '', html, flags=re.DOTALL)
# Remove .photo-frame and .photo-frame::after rules
html = re.sub(r'\.photo-frame\{[^}]*\}', '', html)
html = re.sub(r'\.photo-frame::after\{[^}]*\}', '', html, flags=re.DOTALL)

# Make hero grid single column since no photo
html = html.replace('grid-template-columns:1fr auto', 'grid-template-columns:1fr')
html = html.replace('gap:60px;align-items:center', 'gap:20px')
html = html.replace('justify-items:center', '')

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Image removed")
