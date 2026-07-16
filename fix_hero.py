import os, re

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the entire hero section
old_hero = '''<header class="hero"><div class="wrap hero-grid"><div class="reveal"><span class="badge"><span class="dot"></span> open to remote &amp; UAE roles</span><h1>Biswash <span class="grad">Rai</span></h1><p class="role">AI Automation Engineer &amp; Digital Operations Consultant</p>
<div class="glow-line"><span class="glow-word">n8n</span><span class="glow-word">crewai</span><span class="glow-word">supabase</span><span class="glow-word">fastapi</span><span class="glow-word">llms</span><span class="glow-word">webhooks</span></div><p class="lede">I design, orchestrate, and deploy production-grade multi-agent LLM systems and self-healing automation pipelines - turning complex manual operations into autonomous digital infrastructure. Known in the dev community as <strong>@vibetechbee</strong>.</p><div class="photo-frame"><img src="profile.png" alt="Biswash Rai" /></div>
      <div class="hero-actions"><a class="btn btn-primary" href="#projects">View Projects </a><a class="btn btn-ghost" href="mailto:biswashrai04@gmail.com">Email Me</a></div></div></div></header>'''

new_hero = '''<header class="hero"><div class="wrap hero-grid"><div class="reveal"><span class="badge"><span class="dot"></span> open to remote &amp; UAE roles</span><h1>Biswash <span class="grad">Rai</span></h1><p class="role">AI Automation Engineer &amp; Digital Operations Consultant</p>
<div class="glow-line"><span class="glow-word">n8n</span><span class="glow-word">crewai</span><span class="glow-word">supabase</span><span class="glow-word">fastapi</span><span class="glow-word">llms</span><span class="glow-word">webhooks</span></div><p class="lede">I design, orchestrate, and deploy production-grade multi-agent LLM systems and self-healing automation pipelines - turning complex manual operations into autonomous digital infrastructure. Known in the dev community as <strong>@vibetechbee</strong>.</p><div class="hero-actions"><a class="btn btn-primary" href="#projects">View Projects </a><a class="btn btn-ghost" href="mailto:biswashrai04@gmail.com">Email Me</a></div></div><div class="photo-frame"><img src="profile.png" alt="Biswash Rai" /></div></div></header>'''

html = html.replace(old_hero, new_hero)

# Update hero-grid CSS to ensure two columns
html = html.replace('grid-template-columns:1fr auto', 'grid-template-columns:1fr auto')
# Make sure photo is vertically centered
html = html.replace('gap:40px;align-items:center', 'gap:48px;align-items:center')

# Add responsive rule for mobile
html = html.replace('@media(max-width:860px){.hero-grid{grid-template-columns:1fr;gap:44px;text-align:center;justify-items:center}.lede{margin-left:auto;margin-right:auto}}', '@media(max-width:860px){.hero-grid{grid-template-columns:1fr!important;gap:44px;text-align:center;justify-items:center}.lede{margin-left:auto;margin-right:auto}.photo-frame{margin:0 auto}}')

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Hero fixed")
