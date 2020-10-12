import time
import pyautogui


pyautogui.hotkey('winleft', 'r')

time.sleep(0.5)
pyautogui.typewrite("mspaint")
time.sleep(0.5)

pyautogui.press("enter")
time.sleep(1)