from PIL import Image
from pynput.mouse import Listener
from pynput.mouse import Controller
mouse = Controller()

img  = Image.open("test.jpg")
pixel_values = list(img.getdata())
img.show()

def on_click(x, y, button, pressed):
    width, height = img.size
    if pressed:
        print(pixel_values[width*y+x]) #co to kurwa jest

with Listener(on_click = on_click) as listener:
    listener.join()



