import speech_recognition as sr
import pyautogui
import time
import main

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
                pyautogui.press("tab", presses=2, interval=0.1)
                pyautogui.press("enter",presses=3, interval=0.3)
                main.speak(f"Playing {song_name}")
        except Exception as e:
            main.speak("Sorry, I couldn't recognize the song.")
            print("Error:", e)