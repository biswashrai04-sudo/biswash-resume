from PIL import Image, ImageEnhance

im = Image.open(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png").convert("RGB")
im = ImageEnhance.Brightness(im).enhance(1.35)
im = ImageEnhance.Contrast(im).enhance(1.15)
im = ImageEnhance.Sharpness(im).enhance(1.10)
r, g, b = im.split()
r = r.point(lambda x: min(255, int(x * 1.05)))
im = Image.merge("RGB", (r, g, b))
im.save(r"C:\Users\dell\Documents\Biswash_Resume\web-resume\profile.png", "PNG")
print("Image enhanced")
