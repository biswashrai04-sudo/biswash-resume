from PIL import Image, ImageEnhance

im = Image.open(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png").convert("RGB")
# Natural, balanced brightness
im = ImageEnhance.Brightness(im).enhance(1.02)
im = ImageEnhance.Contrast(im).enhance(1.20)
im = ImageEnhance.Sharpness(im).enhance(1.08)
im.save(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png", "PNG")
print("Done - natural balance")
