import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Find and replace hero section
hero_start = html.index('<header class="hero">')
hero_end = html.index('</header>') + len('</header>')

new_hero = '''<header class="hero">
  <div class="wrap hero-grid">
    <div class="reveal">
      <span class="badge"><span class="dot"></span> open to remote &amp; UAE roles</span>
      <h1>Biswash <span class="grad">Rai</span></h1>
      <p class="role">AI Automation Engineer &amp; Digital Operations Consultant</p>
      <div class="glow-line">
        <span class="glow-word">n8n</span>
        <span class="glow-word">crewai</span>
        <span class="glow-word">supabase</span>
        <span class="glow-word">fastapi</span>
        <span class="glow-word">llms</span>
        <span class="glow-word">webhooks</span>
      </div>
      <p class="lede">I design, orchestrate, and deploy production-grade multi-agent LLM systems and self-healing automation pipelines — turning complex manual operations into autonomous digital infrastructure. Known in the dev community as <strong>@vibetechbee</strong>.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#projects">View Projects →</a>
        <a class="btn btn-ghost" href="mailto:biswashrai04@gmail.com">Email Me</a>
      </div>
    </div>
    <div class="photo-frame">
      <img src="profile.png" alt="Biswash Rai" />
    </div>
  </div>
</header>'''

html = html[:hero_start] + new_hero + html[hero_end:]

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

# Verify structure
with open(path, "r", encoding="utf-8") as f:
    check = f.read()
hero_check = check[check.index('<header class="hero">'):check.index('</header>')+len('</header>')]
if '<div class="photo-frame">' in hero_check and hero_check.index('<div class="photo-frame">') > hero_check.index('</div>\n    </div>'):
    print("WRONG - photo still inside text div")
else:
    print("OK - photo is in separate grid column")
