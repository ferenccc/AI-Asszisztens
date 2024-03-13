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

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser as wb


engine = pyttsx3.init()

def speak(voice):
    newVoiceRate = 150
    engine.setProperty('rate',newVoiceRate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(voice)
    engine.runAndWait()
 

def idő():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Londoni, időzona szerint")
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
        speak("harmadik hónap azaz Március")
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


def köszönöm():
    speak("Nagyon szívesen.")
    speak(köszönöm)

def welcome():
    speak("Hello.")
    

def scanner():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
 
    with open('adat.txt') as f:
        myDataList = f.read().splitlines()

    IronMan = '5996514018240'
    IronMan2 = '5996514018264'
    IronMan3 = '5996514015041'
    Netflix = '5994100159988'
    Systane = '0300651510782'
    Random = '0787099257798'
    
    scanned = False  # Változó nyomon követi, hogy már történt-e vonalkódolvasás
    
    while not scanned:  # Addig fut a ciklus, amíg nincs vonalkódolvasás
    
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            print(myData)
    
            if myData in (Systane):
                chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                wb.get(chromepath).open_new_tab('https://benu.hu/shop/systane-hydration-tartositoszer-mentes-lubrikalo-szemcsepp-10ml')
                scanned = True  # Beállítjuk, hogy történt vonalkódolvasás
                break  # Kilépünk a for ciklusból, mert már találtunk egy vonalkódot
            elif myData in (Random):
                chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                wb.get(chromepath).open_new_tab('https://adatbank.mlsz.hu/league/61/8/27730/15.html')
                scanned = True
                break 
    
            else:
                print("Nem azonosítható vonalkód.")
    
        cv2.imshow('Result', img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()


        
    

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
    server.login('nadjferenc00@gmail.com','mrifrrbmttutzeet')
    server.sendmail('szedelyimartina@gmail.com', to,content )
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

        
            

        elif 'köszönöm' in query:
            köszönöm()
        elif 'email' in query:
            try:
                speak("Mit mondjak?")
                content = takeCommand()
                
                to = 'szedelyimartina@gmail.com'
                
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
        elif 'szkenner' in query:
            scanner()        
        elif 'vicc' in query:
            jokes()
        elif 'pihenj' in query:
            speak("Rendben")
            quit()