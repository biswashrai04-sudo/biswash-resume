import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace glow-word CSS with glassmorphism
old_glow = """.glow-word{
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
.glow-word:nth-child(6){animation-delay:2.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.12);background:rgba(224,160,92,.04)}"""

new_glow = """.glow-word{
  font-family:var(--mono);font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;
  padding:5px 12px;border-radius:8px;
  background:rgba(26,22,38,.5);
  backdrop-filter:blur(12px);
  -webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(176,124,232,.18);
  color:var(--accent-soft);
  box-shadow:0 0 10px rgba(176,124,232,.1),inset 0 0 8px rgba(176,124,232,.05);
  animation:dimGlow 3s ease-in-out infinite alternate;
}
.glow-word:nth-child(2){animation-delay:.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.18);box-shadow:0 0 10px rgba(224,160,92,.1),inset 0 0 8px rgba(224,160,92,.05)}
.glow-word:nth-child(3){animation-delay:1s}
.glow-word:nth-child(4){animation-delay:1.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.18);box-shadow:0 0 10px rgba(224,160,92,.1),inset 0 0 8px rgba(224,160,92,.05)}
.glow-word:nth-child(5){animation-delay:2s}
.glow-word:nth-child(6){animation-delay:2.5s;color:var(--primary-soft);border-color:rgba(224,160,92,.18);box-shadow:0 0 10px rgba(224,160,92,.1),inset 0 0 8px rgba(224,160,92,.05)}"""

html = html.replace(old_glow, new_glow)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Glow words glass applied")
