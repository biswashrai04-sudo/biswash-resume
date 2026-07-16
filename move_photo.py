import os
path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Ensure hero grid has two columns: text left, photo right
html = html.replace('grid-template-columns:1fr', 'grid-template-columns:1fr auto', 1)

# Make sure hero-grid has proper alignment
html = html.replace('gap:20px', 'gap:40px;align-items:center', 1)

# Move photo div to be after hero-actions but inside reveal div
# First remove old photo placement if any
import re
html = re.sub(r'<div class="photo-frame">.*?</div>\s*(?=<div class="hero-actions">)', '', html, flags=re.DOTALL)

# Add photo after lede paragraph, before hero-actions
lede_end = '<div class="hero-actions">'
photo_div = '<div class="photo-frame"><img src="profile.png" alt="Biswash Rai" /></div>'
html = html.replace(lede_end, photo_div + '\n      ' + lede_end)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Photo moved to right")
