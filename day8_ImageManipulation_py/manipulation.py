from PIL import Image, ImageFilter
import os



image1 = Image.open('Food.jpg')
image1.rotate(90).save('Food_mod.jpg')
image1.convert(mode='L').save('Food_mod_w.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('Food_mod_b.jpg')