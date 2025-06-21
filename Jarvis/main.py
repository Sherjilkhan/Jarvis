import speech_recognition as sr 
import pyttsx3                 
import Commands                 

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer() # Creates a Recognizer object for speech recognition
engine = pyttsx3.init()      # Initializes the Text-to-Speech engine

# Global Assistant response function
def speak(text):
    """
    Converts the given text to speech and prints it to the console.

    Args:
        text (str): The text to be spoken.
    """
    print("Jarvis:", text) # Prints the assistant's response to the console
    engine.say(text)       # Adds text to the speech queue
    engine.runAndWait()    # Blocks while all speech is being generated

# Main Loop
if __name__ == "__main__":
    """
    The main execution loop of the Jarvis assistant.
    It continuously listens for the wake word "Jarvis" and then processes commands.
    """
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    while True: # Infinite loop for continuous listening
        try:
            with sr.Microphone() as source: # Uses the default microphone as audio source
                print("Listening for wake word...")
                # Adjust for ambient noise and listen for a short duration for the wake word
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=1)
                trigger = recognizer.recognize_google(audio).lower() # Recognizes speech using Google Speech Recognition

            if "jarvis" in trigger: # Checks if the wake word is detected
                speak("Yes Master Sherjil")
                with sr.Microphone() as source: # Listens for the command after the wake word
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=1) # Listen for command for a longer duration
                    command = recognizer.recognize_google(audio) # Recognizes the command
                    Commands.processCommand(command) # Passes the command to the processCommand function

        except sr.UnknownValueError:
            # Handles cases where the speech recognizer could not understand the audio
            print("Didn't understand the wake word.")
        except sr.WaitTimeoutError:
            # Handles cases where no speech was detected within the timeout period
            print("Listening timed out...")
        except Exception as e:
            # Catches any other unexpected errors
            print(f"Error: {e}")