import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as key
import pyautogui as pyauto


class Controller:
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = key()    
        self.py = pyauto
    
    def move_mouse_press(self, x,y):
        self.keyboard.press('q')
        self.keyboard.release('q')
        self.mouse.position = (int(x), int(y))
        self.py.moveTo(x,y,2)
        self.py.click(x,y)
        pyauto.mouseDown()
        pyauto.mouseUp(x,y)
        pyauto.click()
        time.sleep(1)
        

 
    def leave(self):
        self.keyboard.press(Key.f3)
        self.keyboard.release(Key.f3)
        time.sleep(0.5)
        
