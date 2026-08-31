import pyautogui
import time

def SpamPinginator():
    ping = input("What should I spam: ")
    spam = int(input("How many times: "))

    print("You have 5 seconds to click into the window...")
    time.sleep(5)

    for i in range(spam):
        pyautogui.typewrite(ping)
        time.sleep(0.1)
        pyautogui.press("enter")

SpamPinginator()

#added functionality to allow user to say how many times they want to spam the victim, although discord does get mad after a certain point
