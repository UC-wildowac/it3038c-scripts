#This first python extension blurs an image
from PIL import Image, ImageFilter
OriImage = Image.open(r'C:\Users\wildw\Desktop\Test image.JPG')
blurImage = OriImage.filter(ImageFilter.BLUR)
blurImage.show()


#This next one creates an image thumbnail to the spec that youtube has
from PIL import Image
def tnails():
      image = Image.open(r'C:\Users\wildw\Desktop\Test image 2.JPG')
      image.thumbnail((1280,720))
      image.save(r'C:\Users\wildw\Desktop\Test images\Test image 2 thumbnail.JPG')
      image1 = Image.open(r'C:\Users\wildw\Desktop\Test images\Test image 2 thumbnail.JPG')
      image1.show()
tnails()


#This last one applies a sharpen filter to the image, but I 
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   CONTOUR
)
img = Image.open(r'C:\Users\wildw\Desktop\Test image 3.JPG')
img1 = img.filter(CONTOUR)
img1.save(r'C:\Users\wildw\Desktop\Test image 3 sharpened.JPG')
img1.show()