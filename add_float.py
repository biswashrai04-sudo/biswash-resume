import os
path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Add floating animation CSS
float_css = """
/* -------- FLOATING PHOTO -------- */
@keyframes float{
  0%{transform:translateY(0px) rotate(0deg)}
  25%{transform:translateY(-8px) rotate(0.5deg)}
  50%{transform:translateY(-14px) rotate(0deg)}
  75%{transform:translateY(-8px) rotate(-0.5deg)}
  100%{transform:translateY(0px) rotate(0deg)}
}
.photo-frame{animation:float 6s ease-in-out infinite}
.photo-frame::after{
  content:"";
  position:absolute;inset:-1px;border-radius:var(--radius-lg);
  box-shadow:0 28px 70px -20px rgba(176,124,232,.35);
  z-index:-1;
  animation:shadowPulse 6s ease-in-out infinite;
}
@keyframes shadowPulse{
  0%{box-shadow:0 28px 70px -20px rgba(176,124,232,.25);transform:scale(1)}
  50%{box-shadow:0 40px 90px -20px rgba(176,124,232,.45);transform:scale(1.02)}
  100%{box-shadow:0 28px 70px -20px rgba(176,124,232,.25);transform:scale(1)}
}
"""
html = html.replace("/* -------- GLOW TEXT -------- */", float_css + "\n/* -------- GLOW TEXT -------- */")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Float animation added")
