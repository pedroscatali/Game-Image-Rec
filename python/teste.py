import cv2 as cv
import numpy as np
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as key
import pyautogui as pyauto

mouse = MouseController()
keyboard = key()
haystack_img = cv.imread('Imgp.jpg', cv.IMREAD_UNCHANGED)
haystack_img = np.uint8(haystack_img )
k= cv.cvtColor(haystack_img, cv.COLOR_RGB2HSV_FULL)

cv.imshow('w', haystack_img)

cv.imshow('k', haystack_img)
color1 = np.array([0, 0, 255])

color = np.uint8([[[253, 242, 246]]])


mask = cv.inRange(k, color1, color1)
cv.waitKey()

cv.imshow('w', mask)

cv.waitKey()
res = cv.bitwise_and(haystack_img, haystack_img, mask=mask)
cv.imshow('w', res)
cv.waitKey()
 

needle_img = cv.imread('InI1R.png', cv.IMREAD_COLOR)



cv.imshow('w', res)
cv.waitKey()


x = 0



while x<=5:
    result = cv.matchTemplate(res,needle_img,cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(max_loc)
    print(min_loc)
    print('best: %s' % str(max_loc))
    print(' best max confidence %s' % max_val )
    k = int((max_loc[0]+min_loc[0])/2)
    y = int((max_loc[1]+min_loc[1])/2)
    print(k)
    print(y)
    threshold = 0.4
    if max_val>=threshold:
        print('match found')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]
        
        top_left = max_loc
        bottom_right= (top_left[0] + needle_w,top_left[1] + needle_h)
        print(bottom_right)
        pos = (int((bottom_right[0]+max_loc[0])/2),
               int((bottom_right[1]+max_loc[1])/2))
        print(pos)
        cv.rectangle(res, top_left, bottom_right,
                        color=(255,255,255),thickness=2, lineType=cv.LINE_4)
        cv.imshow('Result', result)
        cv.waitKey()
        cv.imshow('Result',res)
        cv.waitKey()
        x +=1
        
         
        
        keyboard.press('q')
        keyboard.release('q')
        mouse.position = (int(pos[0]),
                         int(pos[1]))
        mouse.click(Button.left)
    else:
        print('not found')
        x +=1


