import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init()

def speak(voice):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(voice)
    engine.runAndWait()
 

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(year)
    speak(month)
    speak(date)

def wishme():
    speak("Welcome back Mr.Stark")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    elif hour >=18 and hour<24:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("How can I help you?")

def hello():
    speak("Hello Mr.Stark, how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hallgatom...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Egy pillanat...")
        query = r.recognize_google(audio, language ='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Can you repeat it?...")

        return "None"        
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nadjferenc00@gmail.com', 'ferencke')
    server.sendmail('dorasamu@icloud.com', to,content )
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            idő()

        elif 'date' in query:
            dátum() 
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'kacsataska1015@gmail.com'
                sendemail(to,content)
                
                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to sent email")
        
        elif 'search in chrome' in query:
            speak("What should I search for ?")
            chromepath = 'C:/Program Filesc (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'offline' in query:
            quit()



