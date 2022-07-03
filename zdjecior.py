from PIL import Image

img  = Image.open("test.jpg")
width, height = img.size
x = int(input('Podaj koordynat x:'))
y = int(input('Podaj koordynat y:'))
pixel_values = list(img.getdata())
print(pixel_values[width*y+x])