import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
from selenium import webdriver
import pyautogui as pg
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! , Sir harsh")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! , Sir harsh")   

    else:
        speak("Good Evening! , Sir harsh")  

    speak("I am your assistant sir, please tell me the work to do.")       

def sun():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = sun().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'whatsapp' in query:
            print("please say the number to which you want to send the message and speak slowly . ")
            numm =  sun()
            nummm = numm + "+91"
            print("say your msg ")
            msgg = sun()
            webbrowser.open('https://web.whatsapp.com/send?phone='+nummm+'&text='+msgg)
            time.sleep(4)
            pg.press('enter')
        