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
    speak("Budapesti időzona szerint")
    speak(Time)

def dátum():
    year = int(datetime.datetime.now().year)
    month= str(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("A mai dátum: ")
    speak(year)
    speak(month+'dik hó')
    speak(date)

def wishme():
    speak("Üdvözlöm Miszter Stark")
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

def köszönöm():
    speak("Nagyon szívesen.")
    speak(köszönöm)

def welcome():
    speak("Jó napot!")
    

def vagyok():
    speak("Üdvözlöm Miszisz Dóra.")
    speak(vagyok)

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
    server.login('nadjferenc00@gmail.com', 'ferencke')
    server.sendmail('nadjferenc00@gmail.com', to, content )
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

def buek():
    speak("Üdv!")

def scanner():
    os.system('scanner3.py')

if __name__ == "__main__":
    
    while True:
        buek()
        query = takeCommand().lower()

        if "idő" in query:
            idő()

        elif "sorozat" in query:
            video()

        elif 'dátum' in query:
            dátum() 
        elif 'wikipedia' in query:
            speak("Keresés...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'valamit' in query:
            valamit()
        elif 'vagyok' in query:
            vagyok()
        elif 'köszönöm' in query:
            köszönöm()
        elif 'levél' in query:
            try:
                speak("Mit mondjak?")
                content = takeCommand()
                to = 'nadjferenc00@gmail.com'
                
                sendemail(to,content)
                
                speak("A levél elküldve.")
            except Exception as e:
                print(e)
                speak("Unable to sent email")
        elif 'keresés web' in query:
            speak('Mire keressek rá ?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif 'weather' in query:
            speak('Nézzük csak.')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab('idokep.hu')
            takeCommand().lower()
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t l") 
        
        elif 'restart' in query:
            os.system("shutdown /r /t l")

        elif 'adatok' in query:
            wishme()

        elif 'nyomjunk zenét' in query:
            songs_dir = 'C:/Users/nadjf/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        
        elif 'írd fel amit mondok' in query:
            speak("Hallgatom Miszter Stark.")
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

        elif 'scan' in query:
            scanner()
        elif 'dobjál be egy whiskyt' in query:
            speak("Rendben")
            quit()


