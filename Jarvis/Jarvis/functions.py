import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import os
import pyautogui
import time
import keyboard
import main 
from datetime import datetime
import google.generativeai as genai

# api key = AIzaSyBLnlLUM_iwB3oQHJxVbJlCxXyWbNjkmq8
################| Google  functions |################

def google_func():
    main.speak("Opening Google...")
    webbrowser.open("https://google.com")
    time.sleep(1)
    try:
            with sr.Microphone() as source:
                main.speak("What are you looking for?")                         
                search_input = main.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                search = main.recognizer.recognize_google(search_input)
                main.speak(f"Searching for {search} on Google")
                time.sleep(0.5)
                pyautogui.write(search, interval=0.1)
                
                time.sleep(1)
                pyautogui.press("enter")                
                main.speak(f"Here is what I found for  {search}")
    except Exception as e:
            main.speak("Sorry, I couldn't recognize the song.")
            print("Error:", e)
     
################| Youtube  functions |################

def youtube_func():
    main.speak("Opening YouTube...")
    webbrowser.open("https://www.youtube.com/")
    time.sleep(1)
    try:
            with sr.Microphone() as source:
                main.speak("What do you wanna watch?")                         
                search_input = main.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                search = main.recognizer.recognize_google(search_input)
                main.speak(f"Searching for {search} on Youtube")
                pyautogui.hotkey("/")                
                time.sleep(0.3)
                pyautogui.write(search, interval=0.1)
                time.sleep(1)
                pyautogui.press("enter")                
                main.speak(f"Here is what I found for  {search}")
    except Exception as e:
            main.speak("Sorry, I couldn't recognize the song.")
            print("Error:", e)
################| Spotify functions |################

def spotify_fnc():
        main.speak("Opening Spotify")
        pyautogui.press("win")
        time.sleep(0.5)
        pyautogui.write("Spotify", interval=0.1)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(5)  # Let it open fully

        try:
            with sr.Microphone() as source:
                main.speak("Which song do you want to listen to?")                         #Selecting song to play 
                song_audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                song_name = main.recognizer.recognize_google(song_audio)
                main.speak(f"Searching for {song_name} on Spotify")
                pyautogui.hotkey("ctrl", "l")
                time.sleep(1)
                pyautogui.write(song_name, interval=0.1)
                time.sleep(2)
                pyautogui.press("enter")
                time.sleep(4)
                pyautogui.press("tab", presses=1, interval=0.5)
                pyautogui.press("enter",presses=2, interval=0.3)
                main.speak(f"Playing {song_name}")
        except Exception as e:
            main.speak("Sorry, I couldn't recognize the song.")
            print("Error:", e)

################| WhatsApp functions |################

def WhatsApp_func():
        main.speak("Opening WhatsApp")
        pyautogui.press("win")
        time.sleep(0.5)
        pyautogui.write("Whatsapp", interval=0.1)
        time.sleep(0.5)
        pyautogui.press("enter")

def Messaging_func():
        try:
            main.speak("Who do you want to send the message to?")
            with sr.Microphone() as source:
                contact_audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=4)
                contact_name = main.recognizer.recognize_google(contact_audio)

            main.speak("What is the message?")
            with sr.Microphone() as source:
                msg_audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=6)
                message = main.recognizer.recognize_google(msg_audio)

            main.speak(f"Sending message to {contact_name}")
            pyautogui.press("win")
            time.sleep(0.5)
            pyautogui.write("Whatsapp", interval=0.1)
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(4)

            pyautogui.hotkey("ctrl", "f")  # focus search bar
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            time.sleep(1)
            pyautogui.write(contact_name, interval=0.1)
            time.sleep(2)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.write(message, interval=0.05)
            pyautogui.press("enter")
            main.speak("Message sent successfully")

        except Exception as e:
            main.speak("Sorry, I couldn't send the message.")
            print("WhatsApp message error:", e)

def voiceCall_func():
        try:
            main.speak("Who do you want to call?")
            with sr.Microphone() as source:
                contact_audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=4)
                contact_name = main.recognizer.recognize_google(contact_audio)

            main.speak(f"Calling {contact_name}")
            pyautogui.press("win")
            time.sleep(0.5)
            pyautogui.write("Whatsapp", interval=0.1)
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(4)

            pyautogui.hotkey("ctrl", "f")
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            time.sleep(1)
            pyautogui.write(contact_name, interval=0.1)
            time.sleep(1)
            
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("tab", presses=11,interval=0.1)  # coordinates for voice call button (adjust if needed)
            pyautogui.press("enter")
            main.speak("Voice call started")

        except Exception as e:
            main.speak("Sorry, I couldn't start the voice call.")
            print("Voice call error:", e)

    
def videoCall_func():
        try:
            main.speak("Who do you want to video call?")
            with sr.Microphone() as source:
                contact_audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=4)
                contact_name = main.recognizer.recognize_google(contact_audio)

            main.speak(f"Starting video call with {contact_name}")
            pyautogui.press("win")
            time.sleep(0.5)
            pyautogui.write("Whatsapp", interval=0.1)
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(4)
            pyautogui.hotkey("ctrl", "f")
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            time.sleep(1)
            pyautogui.write(contact_name, interval=0.1)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("tab", presses=10, interval=0.1)  # coordinates for video call button (adjust if needed)
            pyautogui.press("enter")
            main.speak("Video call started")

        except Exception as e:
            main.speak("Sorry, I couldn't start the video call.")
            print("Video call error:", e)

################| Camera functions |################

def go_to_mode(mode):
    # Go to top (video mode)
    for _ in range(3):
        pyautogui.press("up")
        time.sleep(0.5)

    if mode == "video":
        main.speak("Switched to video mode")
        # Already at video mode
    elif mode == "photo":
        pyautogui.press("down")
        main.speak("Switched to photo mode")
    elif mode == "document":
        pyautogui.press("down")
        time.sleep(0.3)
        pyautogui.press("down")
        main.speak("Switched to document mode")
    time.sleep(1.5)

################| Date-time functions |################

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    main.speak(f"The current time is {current_time}")

def tell_date():
    today = datetime.now()
    date = today.strftime("%A, %d %B %Y")
    main.speak(f"Today is {date}")
    
################|      Gen-AI Chat     |################

genai.configure(api_key="AIzaSyDSxm2SA_mRu1_bn_OmNdOieeazg9kH4O8")
model = genai.GenerativeModel("gemini-pro")
chat= model


def gemini_chat_func():
    
    try:
        main.speak("What do you want to talk about?")
        with sr.Microphone() as source:
            audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            user_text = main.recognizer.recognize_google(audio)
            print("You said:", user_text)
            main.speak(f"You said: {user_text}")

            # Use Gemini
            response = chat.generate_content(user_text)
            reply = response.text

            print("Jarvis:", reply)
            main.speak(reply)
            for model in genai.list_models():
                print(model.name)
    except Exception as e:
        main.speak("Sorry, Jarvis couldn't respond.")
        print("Jarvis Chat Error:", e)
