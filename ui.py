import tkinter as tk
from tkinter import ttk

root = tk.Tk()

activated = False

class Autoclicker:
 def __init__(self, root, on_start):
    self.on_start = on_start
    root.title('Autoclicker prototype')
    window_width = 320
    window_height = 240
    screen_widht = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_widht/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.resizable(False, False)

    root.attributes('-topmost', 1)
    root.attributes('-alpha', 0.7)
  
    message = tk.Label(root, text= "Enter desired cps below:")
    message.pack()

    self.cps_var = tk.StringVar()
    cpsInput = ttk.Entry(root, textvariable=self.cps_var)
    cpsInput.pack(expand=False, side=tk.TOP, )

    Enter_button = ttk.Button(root, text='Enter', command=self.Enter)
    Enter_button.pack(expand=False,side=tk.TOP)

    exit_button = ttk.Button(root, text= 'Exit', command=lambda: root.quit())
    exit_button.pack(expand=False, side=tk.BOTTOM, padx=20, pady=10)

 def Enter(self):
    cps = self.cps_var.get()
    self.on_start(cps)
   