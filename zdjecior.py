from PIL import Image

img  = Image.open("test.jpg")
#img.show()
width = int(input('Podaj koordynat x:'))
height = int(input('Podaj koordynat y:'))
pixel_values = list(img.getdata())
print(pixel_values[width*height])