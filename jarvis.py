import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()

def speak(voice):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(voice)
    engine.runAndWait()
 

def idő():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Londoni időzona szerint")
    speak(Time)

ev2021 = "kétezerhuszonegy"
ho1 = "Január"
ho2 = "Február"
ho3 = "Március"
ho4 = "Április"
ho5 = "Május"
ho6 = "Június"
ho7 = "Július"
ho8 = "Augusztus"
ho9 = "Szeptember"
ho10 = "Október"
ho11 = "November"
ho12 = "December"
nap24 = "huszon negyedike"


def dátum():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("A mai dátum: ")
    if year == 2021:
        speak(ev2021)
    else:
        speak(year)
    
    if month == 1:
        speak(ho1)
    elif month == 2:
        speak(ho2)
    elif month == 3:
        speak(ho3)
    elif month == 4:
        speak(ho4)
    elif month == 5:
        speak(ho5)
    elif month == 6:
        speak(ho6)
    elif month == 7:
        speak(ho7)
    elif month == 8:
        speak(ho8)
    elif month == 9:
        speak(ho9)
    elif month == 10:
        speak(ho10)
    elif month == 11:
        speak(ho11)
    elif month == 12:
        speak(ho12)
    
    if date == 24:
        speak(nap24)
    else:

        speak(date)

def wishme():
    speak("Üdvözlöm Miszter Ferenc")
    idő()
    dátum()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Jó reggelt!")
    elif hour >=12 and hour<18:
        speak("Jó napot!")
    elif hour >=18 and hour<24:
        speak("Jó estét!")
    else:
        speak("Jó éjszakát!")

    speak("Jarvis áll szolgálatára uram, miben segíthetek?")

def valamit():
     speak("Ohh, Boldog Névnapot János!")
     speak(valamit)

def vagyok():
    speak("Üdvözlöm Miszisz Nagy.")
    speak(vagyok)

def köszönöm():
    speak("Nagyon szívesen.")
    speak(köszönöm)

def welcome():
    speak("Hello")
    #dátum()
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hallgatom...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Egy pillanat...")
        query = r.recognize_google(audio, language ='hu-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Ismételje meg kérem...")

        return "None"        
    return query
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nadjferenc00@gmail.com','ferencke')
    server.sendmail('ferencnadj10@icloud.com', to,content )
    server.close()

def képernyőfotó():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\nadjf\\OneDrive\\Dokumentumok\\GYAKORLÁSOK\\JARVIS PROGRAM\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('A CPU állása'+usage)
    battery = str(psutil.sensors_battery())
    speak("Az akkumulátor állása"+battery+"százalék")

def jokes():
    speak(pyjokes.get_jokes())

if __name__ == "__main__":
    welcome()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            idő()

        elif 'dátum' in query:
            dátum() 
        elif 'wikipédia' in query:
            speak("Keresés...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'web' in query:
            
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            speak("Keresés...")
            wb.get(chromepath).open_new_tab(search)
            

        elif 'valamit' in query:
            valamit()
        elif 'vagyok' in query:
            vagyok()
        elif 'köszönöm' in query:
            köszönöm()
        elif 'email' in query:
            try:
                speak("Mit mondjak?")
                content = takeCommand()
                
                to = 'ferencnadj10@icloud.com'
                
                sendemail(to,content)
                
                speak("A levél elküldve.")
            except Exception as e:
                print(e)
                speak("Unable to sent email")
        elif 'keresés weben' in query:
            speak('Mire keressek rá ?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t l") 
        
        elif 'restart' in query:
            os.system("shutdown /r /t l")

        elif 'nyomjunk zenét' in query:
            songs_dir = 'C:/Users/nadjf/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        
        elif 'írd fel amit mondok' in query:
            speak("Hallgatom Mr.Stark.")
            data = takeCommand()
            speak("Az alábbiakat írtam fel"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'jegyzetek' in query:
            remember = open('data.txt','r')
            speak("Az alábbiakat írtam fel" + remember.read())        
        
        elif 'képernyőfotó' in query:
            képernyőfotó()
            speak("Kész!")
        
        elif 'cpu' in query:
            cpu()
        
        elif 'vicc' in query:
            jokes()
        elif 'pihenj' in query:
            speak("Rendben")
            quit()


