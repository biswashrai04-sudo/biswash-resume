import os
path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace("family=Outfit:wght@400;500;600;700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700", "family=Sora:wght@400;500;600;700;800")
html = html.replace('--display:"Outfit","DM Sans",system-ui,sans-serif', '--display:"Sora","Inter",system-ui,sans-serif')
html = html.replace('--body:"DM Sans","Inter",system-ui,sans-serif', '--body:"Sora","Inter",system-ui,sans-serif')
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
ok = "Sora" in html and "Outfit" not in html and "DM Sans" not in html
print("OK" if ok else "PARTIAL - check manually")
