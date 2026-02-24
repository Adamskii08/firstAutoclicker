import pyautogui
import keyboard
import threading
import time
from ui import root, Autoclicker

activated = False

current_cps = None

pyautogui.PAUSE = 0 

#autoclicker logic
def handle_start(cps):
   global current_cps
   current_cps = float(cps)
   

def click_loop():
    while activated:
     pyautogui.leftClick()
     time.sleep(1 / current_cps)

def toggle_loop():
   global activated, thread
   if current_cps is None:
      return
   activated = not activated
   if activated:
      thread = threading.Thread(target=click_loop, daemon=True)
      thread.start()


   
keyboard.add_hotkey('f8', toggle_loop)

app = Autoclicker(root, handle_start)

root.mainloop()