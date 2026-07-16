import os
path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Add simple photo CSS
photo_css = """
/* -------- PHOTO -------- */
.photo-frame{position:relative;width:240px;height:240px;border-radius:var(--radius-lg);overflow:hidden;border:2px solid var(--border)}
.photo-frame img{width:100%;height:100%;object-fit:cover;display:block;filter:brightness(1.0) contrast(1.05)}
"""
html = html.replace("</style>", photo_css + "\n</style>")

# Add photo div after the hero-actions div, before closing hero-grid
photo_html = '<div class="photo-frame"><img src="profile.png" alt="Biswash Rai" /></div>'
html = html.replace('<div class="hero-actions">', '<div class="photo-frame"><img src="profile.png" alt="Biswash Rai" /></div>\n      <div class="hero-actions">')

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Image added back")
