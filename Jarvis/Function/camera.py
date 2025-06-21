import os
import pyautogui
import time
import main 


def go_to_mode(mode):
    # Go to top (video mode)
    for _ in range(3):
        pyautogui.press("up")
        time.sleep(0.5)

    if mode == "video":
        main.speak("Switched to video mode")
        
    elif mode == "photo":
        pyautogui.press("down")
        main.speak("Switched to photo mode")
    elif mode == "document":
        pyautogui.press("down")
        time.sleep(0.3)
        pyautogui.press("down")
        main.speak("Switched to document mode")
    time.sleep(1.5)


def photo():
        main.speak("Opening camera to take a photo")
        os.system("start microsoft.windows.camera:")
        time.sleep(5)
        go_to_mode("photo")
        main.speak("Taking photo in 3 seconds")
        time.sleep(3)
        pyautogui.press("enter")


def video():
        main.speak("Opening camera for video recording")
        os.system("start microsoft.windows.camera:")
        time.sleep(5)
        go_to_mode("video")
        main.speak("Starting video recording")
        time.sleep(2)
        pyautogui.press("enter")