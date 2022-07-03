from PIL import Image
from pynput.mouse import Listener
mouse = Controller()

img  = Image.open("test.jpg")
#img.show()
width = int(input('Podaj koordynat x:'))
height = int(input('Podaj koordynat y:'))

pixel_values = list(img.getdata())


def on_click(x, y, button, pressed):
    if pressed:
        print(pixel_values[width*height])

with Listener(on_click = on_click) as listener:
    listener.join()