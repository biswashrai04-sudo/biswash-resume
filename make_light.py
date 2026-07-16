import os

path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\v2.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Create light version by swapping CSS variables
light_html = html

# Replace dark colors with light colors
replacements = {
    '--canvas:#08060D': '--canvas:#F8F7FC',
    '--surface:#110E1A': '--surface:#FFFFFF',
    '--surface-2:#1A1626': '--surface-2:#F0EDF5',
    '--border:#28223A': '--border:#DDD8E8',
    '--ink:#F0EDF5': '--ink:#1A1626',
    '--muted:#A89FB8': '--muted:#5A5268',
    '--faint:#655D75': '--faint:#8A8298',
    '--primary:#E0A05C': '--primary:#B07CE8',
    '--primary-soft:#F2C88A': '--primary-soft:#9B5FD6',
    '--accent:#B07CE8': '--accent:#E0A05C',
    '--accent-soft:#D4AFFF': '--accent-soft:#C88A3A',
    '--success:#6EC990': '--success:#4CAF7D',
}

for old, new in replacements.items():
    light_html = light_html.replace(old, new)

# Update background glow for light theme
light_html = light_html.replace(
    'rgba(176,124,232,.14),transparent 60%),radial-gradient(45% 35% at 5% 15%,rgba(224,160,92,.09)',
    'rgba(176,124,232,.08),transparent 60%),radial-gradient(45% 35% at 5% 15%,rgba(224,160,92,.06)'
)

# Update glassmorphism for light theme
light_html = light_html.replace('rgba(26,22,38,.55)', 'rgba(255,255,255,.65)')
light_html = light_html.replace('rgba(26,22,38,.7)', 'rgba(255,255,255,.8)')
light_html = light_html.replace('rgba(26,22,38,.5)', 'rgba(255,255,255,.6)')

# Update glow effects for light theme
light_html = light_html.replace('rgba(176,124,232,.12)', 'rgba(176,124,232,.15)')
light_html = light_html.replace('rgba(176,124,232,.25)', 'rgba(176,124,232,.2)')
light_html = light_html.replace('rgba(224,160,92,.15)', 'rgba(224,160,92,.12)')

# Update nav for light theme
light_html = light_html.replace('rgba(8,6,13,.78)', 'rgba(248,247,252,.85)')

# Update btn-primary for light theme (dark text on light bg)
light_html = light_html.replace('color:#0B0A0F', 'color:#FFFFFF')

# Save light version
light_path = r"C:\Users\dell\Documents\Biswash_Resume\web-resume\light.html"
with open(light_path, "w", encoding="utf-8") as f:
    f.write(light_html)

print("Light version saved")
