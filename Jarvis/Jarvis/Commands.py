import speech_recognition as sr
import os
import pyautogui
import time
import keyboard
import functions
import main 



def processCommand(c):
    c = c.lower()
    if "open appnme" in c:
        print


    elif "open google" in c:
        functions.google_func()

    elif "open youtube" in c:
       functions.youtube_func()



    elif "take photo" in c:
        main.speak("Opening camera to take a photo")
        os.system("start microsoft.windows.camera:")
        time.sleep(5)

        functions.go_to_mode("photo")
        main.speak("Taking photo in 3 seconds")
        time.sleep(3)
        pyautogui.press("enter")

    elif "record video" in c:
        main.speak("Opening camera for video recording")
        os.system("start microsoft.windows.camera:")
        time.sleep(5)

        functions.go_to_mode("video")
        main.speak("Starting video recording")
        time.sleep(2)
        pyautogui.press("enter")

    elif "finish recording"  in c:
        main.speak("Stopping video recording")
        pyautogui.press("enter")

    elif "finish recording" in c:
        main.speak("Stopping video recording")
        pyautogui.press("enter")

    elif "open whatsapp" in c:
        functions.WhatsApp_func()
    elif "send message" in c:
        functions.Messaging_func()

    elif "voice call" in c:

        functions.voiceCall_func()

    elif "video call" in c:
        functions.videoCall_func()

    elif "open spotify" in c:
        functions.spotify_fnc()


    elif "pause music" in c or "pause song" in c:
        main.speak("Pausing music")
        keyboard.send("play/pause media")

    elif "play music" in c or "resume music" in c:
        main.speak("Resuming music")
        keyboard.send("play/pause media")

    elif "next song" in c or "skip song" in c:
        main.speak("Skipping to next song")
        keyboard.send("next track")

    elif "previous song" in c or "last song" in c:
        main.speak("Playing previous song")
        keyboard.send("previous track")

    elif "increase volume" in c:
        main.speak("Increasing volume")
        for _ in range(5):
            keyboard.send("volume up")
            time.sleep(0.1)

    elif "decrease volume" in c:
        main.speak("Decreasing volume")
        for _ in range(5):
            keyboard.send("volume down")
            time.sleep(0.1)

    elif "what is the time" in c :
        functions.tell_time()

    elif "what is the date" in c :
        functions.tell_date()

    elif "let's talk" in c or "chat" in c:
        functions.gemini_chat_func()

    elif "terminate" in c or "stop" in c:
        main.speak("Goodbye Master Sherjil!")
        exit()

    else:
        main.speak("I didn't understand your command.")
