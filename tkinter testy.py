import tkinter as tk
from pynput.mouse import Listener
from pynput.mouse import Controller
from pynput.keyboard import Key
root=tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-alpha', 1)
message = tk.Label(root, text = 'e spysz')
message.pack()
root.mainloop()