from PIL import Image, ImageEnhance

im = Image.open(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png").convert("RGB")
im = ImageEnhance.Brightness(im).enhance(0.92)
im = ImageEnhance.Contrast(im).enhance(1.25)
im = ImageEnhance.Sharpness(im).enhance(1.08)
im.save(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png", "PNG")
print("Done - darker")
