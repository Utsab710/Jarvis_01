from time import strftime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")

MASTER = "Utsab"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    
    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour >=12 and hour<18:
        speak("Good Afternoon"+ MASTER)

    else:
        speak("Good Evening"+MASTER)

    speak("I am Jarvis from Iron Man.How may I help you Utsab sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)


    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-nep')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None

    return query

speak("Initializing Jarvis...")
wishMe()
query = takeCommand()

if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
     #webbrowser.open("youtube.com")
     url = "youtube.com"
     brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
     webbrowser.get(brave_path).open(url)
elif 'open google' in query.lower():
     #webbrowser.open("youtube.com")
     url = "google.com"
     brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
     webbrowser.get(brave_path).open(url)
     
elif 'play music' in query:
         music_dir = 'C:\\Users\\ACER\\Downloads\\Music'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))
elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")