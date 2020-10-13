import time
import pyautogui
import keyboard
import random

time.sleep(5)
distance = 500
x = 500
y = 0
while distance > 0:
        if keyboard.is_pressed('p'):
                while True:
                      if keyboard.is_pressed('r'):
                              break

        pyautogui.drag(int(x/2), int(-y/2), duration=0.1)   # move right
        y-=20
        pyautogui.drag(int(x/2), int(y/2), duration=0.1)   # move down
        x -= 10
        pyautogui.drag(-x,0, duration=0.1)  # move up

        if keyboard.is_pressed('x'):
                x= random.randint(0,200)
                y = 0
        if keyboard.is_pressed('y'):
                y= random.randint(0,200)

