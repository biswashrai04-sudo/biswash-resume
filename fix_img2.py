from PIL import Image, ImageEnhance

im = Image.open(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png").convert("RGB")
# Reduce brightness to a balanced level
im = ImageEnhance.Brightness(im).enhance(1.10)
im = ImageEnhance.Contrast(im).enhance(1.18)
im = ImageEnhance.Sharpness(im).enhance(1.05)
im.save(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png", "PNG")
print("Brightness reduced")
