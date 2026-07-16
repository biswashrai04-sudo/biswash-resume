import os
path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Add glow text CSS before the closing </style> tag
glow_css = """
/* -------- GLOW TEXT -------- */
.glow-line{display:flex;flex-wrap:wrap;gap:14px 28px;margin-top:18px;pointer-events:none}
.glow-word{
  font-family:var(--mono);font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;
  padding:5px 12px;border-radius:6px;
  background:rgba(176,124,232,.04);
  border:1px solid rgba(176,124,232,.1);
  color:var(--accent-soft);
  animation:dimGlow 3s ease-in-out infinite alternate;
}
.glow-word:nth-child(2){animation-delay:.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.12);background:rgba(224,160,92,.04)}
.glow-word:nth-child(3){animation-delay:1s}
.glow-word:nth-child(4){animation-delay:1.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.12);background:rgba(224,160,92,.04)}
.glow-word:nth-child(5){animation-delay:2s}
.glow-word:nth-child(6){animation-delay:2.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.12);background:rgba(224,160,92,.04)}

@keyframes dimGlow{
  0%{box-shadow:0 0 4px rgba(176,124,232,.15);opacity:.7}
  50%{box-shadow:0 0 12px rgba(176,124,232,.25);opacity:1}
  100%{box-shadow:0 0 4px rgba(176,124,232,.15);opacity:.7}
}

/* Floating micro labels */
.micro-float{
  position:fixed;pointer-events:none;z-index:2;
  font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--faint);opacity:.35;
  animation:floatSlow 8s ease-in-out infinite alternate;
}
.micro-float.tl{top:30%;left:24px;writing-mode:vertical-rl;animation-delay:0s}
.micro-float.br{bottom:30%;right:24px;writing-mode:vertical-rl;animation-delay:3s}
.micro-float.bl{bottom:18%;left:24px;animation-delay:1.5s;writing-mode:horizontal-tb}
@keyframes floatSlow{0%{opacity:.2;transform:translateY(0)}50%{opacity:.4}100%{opacity:.2;transform:translateY(-6px)}}

/* Footer glow */
.footer-glow{
  text-align:center;padding:0 0 30px;
  font-family:var(--mono);font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent-soft);opacity:.4;
  animation:pulseGlow 4s ease-in-out infinite alternate;
}
@keyframes pulseGlow{0%{text-shadow:0 0 8px rgba(176,124,232,.2)}100%{text-shadow:0 0 18px rgba(176,124,232,.45)}}
"""
html = html.replace("</style>", glow_css + "\n</style>")

# Add glow-line after the role paragraph in hero
hero_html = '<p class="role">AI Automation Engineer &amp; Digital Operations Consultant</p>'
glow_words = '<div class="glow-line"><span class="glow-word">n8n</span><span class="glow-word">crewai</span><span class="glow-word">supabase</span><span class="glow-word">fastapi</span><span class="glow-word">llms</span><span class="glow-word">webhooks</span></div>'
html = html.replace(hero_html, hero_html + "\n" + glow_words)

# Add floating micro labels before </body>
float_html = """<span class="micro-float tl">systems · automation · ai</span>
<span class="micro-float br">build in public</span>
<span class="micro-float bl">@vibetechbee</span>"""
html = html.replace("</body>", float_html + "\n</body>")

# Add footer glow before </footer>
footer_glow = '<div class="footer-glow">designed with precision · built with purpose</div>'
html = html.replace("</footer>", footer_glow + "\n</footer>")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
