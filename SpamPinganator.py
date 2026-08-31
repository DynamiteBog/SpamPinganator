import pyautogui
import time

def SpamPinginator():
    x = 0
    y = 100
    z = 1
    time.sleep(5)
    for i in range(x, y, z):
        pyautogui.typewrite("@ChudGPT")
        pyautogui.press("enter")

SpamPinginator()