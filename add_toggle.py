import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Add theme toggle button to nav
nav_cta = '<a class="nav-cta" href="mailto:biswashrai04@gmail.com">Get in touch</a>'
theme_btn = '''<button class="theme-toggle" onclick="toggleTheme()" title="Switch theme">☀</button>
      <a class="nav-cta" href="mailto:biswashrai04@gmail.com">Get in touch</a>'''
html = html.replace(nav_cta, theme_btn)

# Add theme toggle CSS
toggle_css = """
/* -------- THEME TOGGLE -------- */
.theme-toggle{
  background:var(--surface-2);border:1px solid var(--border);color:var(--muted);
  width:36px;height:36px;border-radius:50%;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:1rem;
  transition:all .3s var(--ease);
}
.theme-toggle:hover{border-color:var(--primary);color:var(--ink);transform:rotate(30deg)}
html.light{--canvas:#F8F7FC;--surface:#FFFFFF;--surface-2:#F0EDF5;--border:#DDD8E8;--ink:#1A1626;--muted:#5A5268;--faint:#8A8298;--primary:#B07CE8;--primary-soft:#9B5FD6;--accent:#E0A05C;--accent-soft:#C88A3A;--success:#4CAF7D}
html.light body::before{background:radial-gradient(55% 45% at 85% -8%,rgba(176,124,232,.06),transparent 60%),radial-gradient(45% 35% at 5% 15%,rgba(224,160,92,.04),transparent 55%)}
html.light nav{background:rgba(248,247,252,.88)}
html.light .chip{background:rgba(255,255,255,.7)!important;border-color:rgba(176,124,232,.2)!important;box-shadow:0 0 8px rgba(176,124,232,.08)!important}
html.light .chip:hover{box-shadow:0 0 16px rgba(176,124,232,.2)!important}
html.light .glow-word{background:rgba(255,255,255,.6)!important;border-color:rgba(176,124,232,.2)!important}
html.light .card{background:#FFFFFF}
html.light .job{background:#FFFFFF}
html.light .btn-primary{background:var(--primary);color:#FFFFFF}
html.light .footer-glow{color:var(--primary-soft)}
"""
html = html.replace("</style>", toggle_css + "\n</style>")

# Add theme toggle script
theme_script = """
function toggleTheme(){
  document.documentElement.classList.toggle('light');
  const btn=document.querySelector('.theme-toggle');
  btn.textContent=document.documentElement.classList.contains('light')?'☾':'☀';
  localStorage.setItem('theme',document.documentElement.classList.contains('light')?'light':'dark');
}
(function(){if(localStorage.getItem('theme')==='light'){document.documentElement.classList.add('light');document.querySelector('.theme-toggle').textContent='☾'}})();
"""
html = html.replace("</script>", theme_script + "\n</script>")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Theme toggle added")
