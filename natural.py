from PIL import Image, ImageEnhance

im = Image.open(r"C:\Users\dell\Documents\Biswash_Resume\edited-photo.png").convert("RGB")
im = ImageEnhance.Brightness(im).enhance(1.0)
im = ImageEnhance.Contrast(im).enhance(1.10)
im = ImageEnhance.Sharpness(im).enhance(1.05)
im.save(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png", "PNG")
print("Natural photo saved")
