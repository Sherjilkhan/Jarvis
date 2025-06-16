import pyautogui
import time
import keyboard
import main 
from Function import whatsapp 
from Function import spotify
from Function import tools
from Function import chatbot
from Function import camera


def processCommand(c):
    c = c.lower()
    if "open appnme" in c:
        print

    elif "open google" in c:
        tools.google_func()

    elif "open youtube" in c:
        tools.youtube_func()

    elif "take photo" in c:
        camera.photo()

    elif "record video" in c:
        camera.video

    elif "finish recording"  in c:
        main.speak("Stopping video recording")
        pyautogui.press("enter")

    elif "open whatsapp" in c:
        whatsapp.WhatsApp_func()

    elif "send message" in c:
        whatsapp.Messaging_func()

    elif "voice call" in c:
        whatsapp.voiceCall_func()

    elif "video call" in c:
        whatsapp.videoCall_func()

    elif "open spotify" in c:
        spotify.spotify_fnc()

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
        tools.tell_time()

    elif "what is the date" in c :
        tools.tell_date()

    elif "let's talk" in c or "chat" in c:
        chatbot.chat()

    elif "terminate" in c or "stop" in c:
        main.speak("Goodbye Master Sherjil!")
        exit()

    else:
        main.speak("I didn't understand your command.")
