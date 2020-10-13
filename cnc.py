import time
import pyautogui
import keyboard

time.sleep(5) # execute paint
distance = 300
while distance > 0:
        if keyboard.is_pressed('p'):
                while True:
                        if keyboard.is_pressed('r'):
                                break

        pyautogui.drag(distance, 0, duration=0.2)   # move right
        distance -= 10
        pyautogui.drag(0, distance, duration=0.2)   # move down
        pyautogui.drag(-distance, 0, duration=0.2)  # move left
        distance -= 10
        pyautogui.drag(0, -distance, duration=0.1)  # move up

