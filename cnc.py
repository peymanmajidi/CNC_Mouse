import time
import pyautogui
import keyboard


# pyautogui.confirm(text='HELLO', title='', buttons=['OK', 'Cancel'])

time.sleep(5)
distance = 500
while distance > 0:
        if keyboard.is_pressed('p'):
                while True:
                      if keyboard.is_pressed('r'):
                              break

        pyautogui.drag(distance, 0, duration=0.1)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.1)   # move down
        pyautogui.drag(-distance, 0, duration=0.1)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.1)  # move up

