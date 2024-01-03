import random

import pyautogui
import pyttsx3

from tkinter.filedialog import *
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import pywhatkit
import random as rd
import wikipedia
import requests
from requests import get
import webbrowser
import pyjokes
import pywhatkit
import smtplib
import sys
import json
import numpy as np
from time import sleep
import instaloader





engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voice[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizeing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")


    except Exception as e:
        speak("say that again please..")
        return "none"
    return query



def wish():
    hour = int(datetime.datetime.now().hour)
    tt =datetime.datetime.now().strftime('%I:%M %p')

    if hour >=0 and hour <=12:
        speak("good morning sir...")


    elif hour >12 and hour <17:
        speak(f"good afternoon sir... Now time {tt}")

    else:
        speak(f"good evening sir...Now time {tt}")

    speak("i am your rocky sir,please tell me how can i help you...")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bharathwajmuthu2004@gmail.com', 'bharathwaj04')
    server.sendmail('vivethamc07@gmail.com', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ca782f299fca42a5a39cd8a2ff7d5da5'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifty","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for a in range(len(day)):
        speak(f"today {day[a]} news is: {head[a]}")

def run_rocky():
    command = takecommand()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        speak('playing'+song)
        pywhatkit.playonyt(song)

def TaskEye():

    while True:
        run_rocky()
        query = takecommand().lower()

        if "open command prompt" in query:
            os.system("start cmd...")
        elif 'play' in query:
            command = takecommand().lower()
            print(command)
            song = command.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
        elif "open camera" in query:
            speak("yes sir opening camera...")
            cap = cv2.VideoCapture(0)
            while True:
                ret,ing = cap.read()
                cv2.imshow('frame',ing)
                if cv2.waitKey(10) == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()
        elif "hai" in query:

            speak("hi,its good to hear from to you")
        elif "who are you" in query:
            speak('iam name is rocky')
        elif "how are you" in query:
            speak('iam fine,thank you for asking This is a challenging time for us.i hope you and your loved ones are staying safe and healthy')
        elif 'date' in query:
            speak('sorry, I have a headache')
        elif 'are you single' in query:
            speak('I am in a relationship with wifi')
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        elif 'open google' in query:
            speak("sir,what should i serach on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/z/")
        elif "send message" in query:
            pywhatkit.sendwhatmsg("+916385429976","this is testing protocol",2,2)

        elif 'open gmail' in query:
            try:
                speak("What should I say SIR")
                content = takecommand()
                to = "vivethamc07@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Gaurav Sir, i am not able to send this email at a moment")
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif "wait for few minutes" in query:

            speak("ok sir,i will be wait !!!")
        elif "you can sleep " in query:
            speak("thanks for using me sir,have a good day...")
            sys.exit()

        elif "close camera" in query:
                speak("okay sir,closing camera...")
                os.system("taskkill /f /im camera.exe")
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn ==22:
                song = query.replace('set alarm ', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.d11,SetSuspendState 0,1,0")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir,feteching the lastest news")
            news()

        elif "where i am" in query or "where we are" in query:
            speak("wait sir,let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure,but i think we are in {city} city of {country} country...")
            except Exception as e:
                speak("sorry sir,Due to network issue i am not able to find where we are...")
                pass

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly...")
            name = input("Enter UersName here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")

            speak("sir would you like to download profile picture of this account...")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("iam am done sir, profile picture is saved in our main folder.now iam ready for next command...")
            else:
                    pass
        elif "take screenshot" in query or "take a screenshot" in query or "take the screenshot" in query:
            speak("Sir,please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds,iam taking screenshot")
            img = pyautogui.screenshot()
            img.save = (f"{name}.png")
            speak("iam am done sir,  the screenshot is saved in our main folder.now iam ready for next command...")

        elif "hide all file" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone...")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir,all the files in this folder are now hidden...")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir,all the files in the folder are now visible to everyone...")
            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")
        elif "scroll" in query:

            speak("yes sir now you will scroll downward are upward")
            cap = cv2.VideoCapture(0)

            yellow_lower = np.array([22, 93, 0])
            yellow_upper = np.array([45, 255, 255])
            prev_y = 0

            while True:
                ret, frame = cap.read()
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                for c in contours:
                    area = cv2.contourArea(c)
                    if area > 300:
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        if y < prev_y:
                            pyautogui.press('space')

                        prev_y = y
                cv2.imshow('frame', frame)
                if cv2.waitKey(10) == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

if __name__ =="__main__":
    wish()








while True:

    TaskEye()
    speak("sir,do you have any other work...")


