import google.generativeai as genai
import speech_recognition as sr
import re
import os
import main 

genai.configure(api_key=os.environ.get("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def chat_with_ai(prompt):
    try:
        response = model.generate_content(prompt)
        clean_response = re.sub(r'[*_~`]', '', response.text)  
        return clean_response
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "There was an error getting a response."
def chat():
    chat_status = True  
    main.speak("I'm listening, go ahead.")
    
    while chat_status:
        try:
           
            print("Listening...")
            with sr.Microphone() as source:
                audio = main.recognizer.listen(source, timeout=5, phrase_time_limit=4)
                prompt = main.recognizer.recognize_google(audio)
                print(f"You said: {prompt}")
                
                if "stop conversation" in prompt.lower() or "stop" in prompt.lower():
                    chat_status = False
                    main.speak("Okay, ending the conversation.")
                    break
                
                ai_response = chat_with_ai(prompt)
                main.speak(ai_response)

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase.")
            main.speak("I didn't hear anything, please try again.")

        except sr.UnknownValueError:
            print("Could not understand audio.")
            main.speak("Sorry, I couldn't understand what you said.")

        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
            main.speak("There's a problem reaching the speech recognition service.")

        except Exception as e:
            print(f"Error: {e}")
            main.speak("Sorry, something went wrong.")

