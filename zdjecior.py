#from os import close
from PIL import Image
from pynput.mouse import Listener
from pynput.mouse import Controller
from pynput.keyboard import Key

mouse = Controller()
keyboard = Controller()

img  = Image.open("test.jpg")

pixel_values = list(img.getdata())
img.show()

def mouse_move(x, y):
    print(x, y)


def on_click(x, y, button, pressed):
    width = mouse.position[0]
    #height = mouse.position[1]
    if pressed:
        print(mouse.position)
        print(pixel_values[width*y+x]) #co to kurwa jest
    return True

#with Listener(on_click = on_click) as listener:
    #listener.join()

with Listener(on_move = mouse_move) as listener:
    listener.join()

while True:
    if keyboard.press(Key.f3):
        quit()
