from PIL import Image
from pynput.mouse import Listener
from pynput.mouse import Controller
mouse = Controller()



img  = Image.open("test.jpg")
#img.show()
#width = int(input('Podaj koordynat x:'))
#height = int(input('Podaj koordynat y:'))

pixel_values = list(img.getdata())

def on_click(x, y, button, pressed):
    if pressed:
        print(mouse.position)

with Listener(on_click = on_click) as listener:
    listener.join()
# width, height = img.size




# x = int(input('Podaj koordynat x:'))
# y = int(input('Podaj koordynat y:'))
# pixel_values = list(img.getdata())
# print(pixel_values[width*y+x])
