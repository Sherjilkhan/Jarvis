import pyautogui
import time
import main 
import speech_recognition as sr

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
