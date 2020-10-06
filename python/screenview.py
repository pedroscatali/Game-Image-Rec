import pyautogui as pyauto
from pynput.keyboard import Key, Controller as key
import win32gui
import win32ui
import win32con
import numpy as np
import cv2 as cv
from time import time
import os
from pynput.mouse import Button, Controller as MouseController
class Screenview:
    
    mouse = MouseController()
    keyboard = key()
    # constructor
    
    

    

    def win_capture(self):
        h= 768  
        w= 1366
        hwnd = win32gui.FindWindow(None, 'Nova Ragnarok')
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(bmp)
        cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

        #screenshot
        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (h, w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(bmp.GetHandle())
        img = img[..., :3]
        img = np.ascontiguousarray(img)
        img = np.uint8(img)
        return img

    def img_compare(self, template):
        
        # get an updated image of the game
        screenshot = self.win_capture()
        #color1 = np.uint8([[[50, 31, 161]]])
        #color = np.uint8([[[253, 242, 246]]])
        #mask = cv.inRange(screenshot, color1, color)
        res = screenshot
        

        haystack_img = cv.imread(template, cv.IMREAD_COLOR)
        haystack_img = np.uint8(haystack_img)
        result1 = cv.matchTemplate(res, haystack_img,cv.TM_CCOEFF_NORMED)

        
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result1)
        print(max_val)
        threshold = 0.4
        if max_val > threshold:
            needle_w = haystack_img.shape[1]
            needle_h = haystack_img.shape[0]
            top_left = max_loc
            bottom_right= (top_left[0] + needle_w,top_left[1] + needle_h)
            pos = (1,int((bottom_right[0]+max_loc[0])/2),int((bottom_right[1]+max_loc[1])/2))
            
            return pos
        else:
            pos = (0,0,0)
            
            return pos
