import speech_recognition as sr
import pyttsx3

import Commands
# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#Global Asistant responce func
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# All the Voice commands

#  Main Loop
if __name__ == "__main__":
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=1 , phrase_time_limit=1)
                trigger = recognizer.recognize_google(audio).lower()

            if "jarvis" in trigger:
                speak("Yes Master Sherjil")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=1)
                    command = recognizer.recognize_google(audio)
                    Commands.processCommand(command)

        except sr.UnknownValueError:
            print("Didn't understand the wake word.")
        except sr.WaitTimeoutError:
            print("Listening timed out...")
        except Exception as e:
            print(f"Error: {e}")
