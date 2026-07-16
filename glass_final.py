import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Force inject glassmorphism CSS right before </style> as a new block
glass_override = """
/* === GLASSMORPHISM OVERRIDE === */
.chip, .chip:hover, .chip:focus {
  background: rgba(26,22,38,.55) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(176,124,232,.22) !important;
  box-shadow: 0 0 10px rgba(176,124,232,.12), inset 0 0 8px rgba(176,124,232,.06) !important;
  transition: all .3s cubic-bezier(.22,.61,.36,1) !important;
}
.chip:hover {
  border-color: rgba(176,124,232,.5) !important;
  box-shadow: 0 0 22px rgba(176,124,232,.35), inset 0 0 14px rgba(176,124,232,.1) !important;
  transform: translateY(-2px) !important;
  color: var(--ink) !important;
}
.glow-word, .glow-word:nth-child(n) {
  background: rgba(26,22,38,.55) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(176,124,232,.22) !important;
  box-shadow: 0 0 12px rgba(176,124,232,.15), inset 0 0 10px rgba(176,124,232,.08) !important;
}
.glow-word:nth-child(2), .glow-word:nth-child(4), .glow-word:nth-child(6) {
  border-color: rgba(224,160,92,.22) !important;
  box-shadow: 0 0 12px rgba(224,160,92,.15), inset 0 0 10px rgba(224,160,92,.08) !important;
}
/* === END GLASSMORPHISM === */
"""
html = html.replace("</style>", glass_override + "\n</style>")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Glass override injected")
