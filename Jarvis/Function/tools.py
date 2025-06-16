import speech_recognition as sr
import main 
from datetime import datetime
import google.generativeai as genai
import os
import time
import webbrowser

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    main.speak(f"The current time is {current_time}")

def tell_date():
    today = datetime.now()
    date = today.strftime("%A, %d %B %Y")
    main.speak(f"Today is {date}")

def calculator():
    main.speak("What operation do you want to perform?")
    try:
        with sr.Microphone() as source:
            audio = main.recognizer.listen(source, timeout=5)
            query = main.recognizer.recognize_google(audio)
            result = eval(query)
            main.speak(f"The result is {result}")
    except Exception as e:
        print("Calculator error:", e)
        main.speak("Sorry, I couldn't perform that calculation.")

# generating weather forecast using gemini api
genai.configure(api_key=os.environ.get("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def weather_ai(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating weather report: {e}")
        return "There was an error getting a response."


def get_weather():
    
    main.speak("Which city would you like the weather forecast for?")
    try:
        with sr.Microphone() as source:
            audio = main.recognizer.listen(source, timeout=5)
            city = main.recognizer.recognize_google(audio)
        weather = weather_ai(f"tell me a short weather report for {city}")
        main.speak(weather)
        
    except Exception as e:
        print("Weather error:", e)
        main.speak("I couldn't fetch the weather right now.")



def google_func():
    
    time.sleep(1)
    try:
            with sr.Microphone() as source:
                main.speak("What are you looking for?")                         
                search_input = main.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                search = main.recognizer.recognize_google(search_input)
                main.speak(f"Searching for {search} on Google")
                webbrowser.open(f"https://www.google.com/search?q={search}&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQw2NjQ3NDIxOGowajeoAgiwAgHxBXkNrGefkaOP&sourceid=chrome&ie=UTF-8")           
                main.speak(f"Here is what I found for  {search}")
    except Exception as e:
            main.speak("Sorry, I couldn't recognize the song.")
            print("Error:", e)
     


def youtube_func():
   
    
    time.sleep(1)
    try:
            with sr.Microphone() as source:
                main.speak("What do you wanna watch?")                         
                search_input = main.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                search = main.recognizer.recognize_google(search_input)
                main.speak(f"Searching for {search} on Youtube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search}")                
                main.speak(f"Here is what I found for  {search}")
    except Exception as e:
            main.speak("Sorry, I couldn't recognize the song.")
            print("Error:", e)
