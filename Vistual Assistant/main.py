
import smtplib
import time
import webbrowser
import datetime
import keyboard
import pyttsx3
import requests
import speech_recognition as sr
import pywhatkit
import wikipedia
import os
import instaloader
from bs4 import BeautifulSoup
from idlist import p, d, g
import Whatsapp
import pyjokes
import psutil
from requests import get

from PyDictionary import PyDictionary as Diction
from ctypes import *

Assistant = pyttsx3.init()
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[7].id)

def Speak(audio):
    print("   ")
    print(f"Jarvis: {audio}")
    Assistant.say(audio)
    print("   ")
    Assistant.runAndWait()

Speak("Initializing Jarvis..")
url = 'http://www.youtube.com/hobbymaster_real'
timeout = 5
try:
    request = requests.get(url,timeout=timeout)
    print("Connected to the internet")
    Speak("Internet connection detected")
    Speak("all systems have been activated")
except (request.ConnectionError, requests.Timeout) as exception:
    print("No Internet Connection")
    Speak("NO internet connection detected")
    Speak("Shutting down the program")
    windll.user32.MessageBoxA(0,'you are not connected to internet, please make sure you are connected to internet')
    Speak("Thanks for giving me your time")
    exit()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        Speak("good morning sir !")

    elif hour>=12 and hour<18:
        Speak("good afternoon sir !")

    else:
        Speak("good Evening sir !" )

    Speak("i am your assistant. How may I help you?")

def music():
    Speak("Tell me the name of the song.")
    musicName = takecommand()
    if 'despacito' in musicName:
        os.openfile('/Users/ramshinde/Downloads/Despacito\(PaglaSongs\).mp3 ')
    else:
        pywhatkit.playonyt(musicName)
        Speak("Your song has been started!, Enjoy Sir")

def Dict():
    Speak("Activated Dictionary")
    Speak("Tell me the problem!")
    prob = takecommand()

    if 'meaning' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of")
        prob = prob.replace("meaning of","")
        result = Diction.meaning(prob)
        Speak(f"The meaning of {prob} is {result} ")

    elif 'synonym' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of")
        prob = prob.replace("synonym of","")
        result = Diction.synonym(prob)
        Speak(f"The synonym of {prob} is {result} ")

    elif 'antonym' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of","")
        prob = prob.replace("antonym of","")
        result = Diction.antonym(prob)
        Speak(f"The antonym of {prob} is {result} ")

def openApps(query):
    Speak('Ok sir, wait a second !')
    if 'whatsapp' in query:
        os.system("open /Applications/WhatsApp.app")
        Speak("Done Sir !")

    elif 'music' in query:
        os.system("open /System/Applications/Music.app")
        Speak("Done Sir !")

    elif 'store' in query:
        os.system("open /System/Applications/App\ Store.app")
        Speak("Done Sir")

    elif 'calculator' in query:
        os.system("open /System/Applications/Calculator.app")
        Speak("Done Sir")

    elif 'java editior' in query:
        os.system("open /Applications/IntelliJ\ IDEA\ CE.app")
        Speak("Done Sir!")

    elif 'photo booth' in query:
        os.system("open /System/Applications/Photo\ Booth.app")
        keyboard.press('enter')
        Speak("Done Sir  !")

    elif 'numbers' in query:
        os.system("open /Applications/Numbers.app ")
        Speak("Done Sir !")

    elif 'keynote' in query:
        os.system("open /Applications/Keynote.app ")
        Speak("Done Sir !")

    elif 'pages' in query:
        os.system("open /Applications/Pages.app")
        Speak("Done Sir !")

    elif 'notes' in query:
        os.system("open /System/Applications/Notes.app")
        Speak("Done Sir !")

    elif 'chrome' in query:
        os.system("open /Applications/Google\ Chrome.app")
        Speak("Done sir !")

    elif 'maps' in query:
        os.system("open /System/Applications/Maps.app")
        Speak("Done Sir !")

    elif 'chess' in query:
        os.system("open /System/Applications/Chess.app ")
        Speak("Done Sir !")

    elif 'photos' in query:
        os.system("open /System/Applications/Photos.app ")
        Speak("Done Sir !")

    elif 'safari' in query:
        os.system("open /Applications/Safari.app ")
        Speak("Done Sir !")

    elif 'podcaste' in query:
        os.system("open /System/Applications/Podcasts.app")
        Speak("Done Sir !")

    elif 'open gmail' in query:
        Speak('opening your google gmail')
        webbrowser.open('https://mail.google.com/mail/')

    elif 'maps' in query:
        Speak('opening google maps')
        webbrowser.open('https://www.google.co.in/maps/')

    elif 'news' in query:
        Speak('opening google news')
        webbrowser.open('https://news.google.com/')

    elif 'calender' in query:
        Speak('opening google calender')
        webbrowser.open('https://calendar.google.com/calendar/')

    elif 'photos' in query:
        Speak('opening your google photos')
        webbrowser.open('https://photos.google.com/')

    elif 'documents' in query:
        Speak('opening your google documents')
        webbrowser.open('https://docs.google.com/document/')

    elif 'spreadsheet' in query:
        Speak('opening your google spreadsheet')
        webbrowser.open('https://docs.google.com/spreadsheets/')

    else :
        No_result_found()

def closeApps(query):
    Speak('Ok sir, wait a second !')
    if 'whatsapp' in query:
        os.system("kill /Applications/WhatsApp.app")
        Speak("Done Sir !")

def social(query):
    print(query)
    if 'facebook' in query:
        Speak('opening your facebook')
        webbrowser.open('https://www.facebook.com/')
    elif 'whatsapp' in query:
        Speak('opening your whatsapp')
        webbrowser.open('https://web.whatsapp.com/')
    elif 'instagram' in query:
        Speak('opening your instagram')
        webbrowser.open('https://www.instagram.com/')
    elif 'twitter' in query:
        Speak('opening your twitter')
        webbrowser.open('https://twitter.com/Suj8_116')
    elif 'discord' in query:
        Speak('opening your discord')
        webbrowser.open('https://discord.com/channels/@me')
    else :
        No_result_found()

def Instagram_Pro():
    Speak("Boss please enter the user name of Instagram: ")
    name = input("Enter username here: ")
    webbrowser.open(f"www.instagram.com/{name}")
    time.sleep(5)
    Speak("Boss would you like to download the profile picture of this account.")
    cond = takecommand()
    if('download' in cond):
        mod = instaloader.Instaloader()
        mod.download_profile(name,profile_pic_only=True)
        Speak("I am done boss, profile picture is saved in your main folder. ")
    else:
        pass


# calender day
def Cal_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)

    return day_of_the_week

def comum(query):
    print(query)
    if ('hi'in query) or('hai'in query) or ('hey'in query) or ('hello' in query) :
        Speak("Hello boss what can I help for u")
    else :
        No_result_found()

#shedule function for remembering todays plans
def shedule():
    day = Cal_day().lower()
    Speak("Boss today's shedule is")
    Week = {"monday" : "Boss from 8:00 to 10:00 you have Python practical, from 10:00 to 11:00 you have Android studio class, from 11:00 to 11:30 you have a recess brake, from 11;30 to 12:30 you have management lecture, from 12:30 to 1:30, from 1:30 to 3:30 you have Android practical and it's time to go home",
    "tuesday" : "Boss from 8:00 to 10:00 you have Python practical, from 10:00 to 11:00 you have ETI lecture, from 11:00 to 11:30 you have a recess brake, from 11;30 to 1:30 you have android practical, from 1:30 to 3:30 you have PHP practical, and it's time to go home",
    "wednesday" : "Remember you have to wear civil dress today, Boss from 8:00 to 10:00 you have Python practical, from 10:00 to 11:00 you have Android studio class, from 11:00 to 11:30 you have a recess brake, from 11;30 to 1:30 you have Android practical, from 1:30 to 3:30 you have EDE practical and it's time to go home",
    "thursday" : " Boss from 8:00 to 9:00 you have Python lecture, from 9:00 to 10:00 you have ETI lecture, from 11:00 to 11:30 you have a recess brake, from 11;30 to 12:30 you have EDE lecture, from 12:30 to 1:30 you have, from 1:30 to 3:30 you have Android practical and it's time to go home",
    "friday" : "Boss from 8:00 to 9:00 you have Python lecture, from 9:00 to 10:00 you have ETI lecture, from 10:00 to 11:00 you have Management lecture, from 11:00 to 11:30 you have a recess brake, from 11;30 to 12:30 you have PHP lecture, from 12:30 to 1:30 you have Android lecture, from 1:30 to 3:30 you have EDE practical and it's time to go home",
    "saturday" : "Boss Today is holiday but you have to complete your submission",
    "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
    if day in Week.keys():
        Speak(Week[day])

#Fun commands to interact with jarvis
def Fun(query):
    print(query)
    if 'your name' in query:
        Speak("My name is jarvis")
    elif 'my name' in query:
        Speak("your name is Shubham")
    elif 'university name' in query:
        Speak("you are studing in Amrita Vishwa Vidyapeetam, with batcheloe in Computer Science and Artificail Intelligence")
    elif 'what can you do' in query:
        Speak("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
    elif 'your age' in query:
        Speak("I am very young that u")
    elif 'date' in query:
        Speak('Sorry not intreseted, I am having headache, we will catch up some other time')
    elif 'are you single' in query:
        Speak('No, I am in a relationship with wifi')
    elif 'joke' in query:
        Speak(pyjokes.get_joke())
    elif 'are you there' in query:
        Speak('Yes boss I am here')
    elif 'tell me something' in query:
        Speak('boss, I don\'t have much to say, you only tell me someting i will give you the company')
    elif 'thank you' in query:
        Speak('boss, I am here to help you..., your welcome')
    elif 'in your free time' in query:
        Speak('boss, I will be listening to all your words')
    elif 'i love you' in query:
        Speak('I love you too boss')
    elif 'can you hear me' in query:
        Speak('Yes Boss, I can hear you')
    elif 'do you ever get tired' in query:
        Speak('It would be impossible to tire of our conversation')
    else :
        No_result_found()

    # System condition
def condition():
    usage = str(psutil.cpu_percent())
    Speak("CPU is at" + usage + " percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    Speak(f"Boss our system have {percentage} percentage Battery")
    if percentage >= 75:
        Speak(f"Boss we could have enough charging to continue our work")
    elif percentage >= 40 and percentage <= 75:
        Speak(f"Boss we should connect out system to charging point to charge our battery")
    elif percentage >= 15 and percentage <= 30:
        Speak(f"Boss we don't have enough power to work, please connect to charging")
    else:
        Speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")


def locaiton():
    Speak("Wait boss, let me check")
    try:
        IP_Address = get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        print(url)
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latidute = geo_data['latitude']
        org = geo_data['organization_name']
        print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
        Speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        Speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        Speak("Sorry boss, due to network issue i am not able to find where we are.")


#Silence
def silence(k):
    t = k
    s = "Ok boss I will be silent for "+str(t/60)+" minutes"
    Speak(s)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    Speak("Boss "+str(k/60)+" minutes over")




    #Time caliculating algorithm
def silenceTime(query):
    print(query)
    x=0
    #caliculating the given time to seconds from the speech commnd string
    if ('10' in query) or ('ten' in query):x=600
    elif '1' in query or ('one' in query):x=60
    elif '2' in query or ('two' in query):x=120
    elif '3' in query or ('three' in query):x=180
    elif '4' in query or ('four' in query):x=240
    elif '5' in query or ('five' in query):x=300
    elif '6' in query or ('six' in query):x=360
    elif '7' in query or ('seven' in query):x=420
    elif '8' in query or ('eight' in query):x=480
    elif '9' in query or ('nine' in query):x=540
    silence(x)

#clock commands
def Clock_time(query):
    print(query)
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    Speak("Current time is "+time)

def OTT(query):
    print(query)
    if 'hotstar' in query:
        Speak('opening your disney plus hotstar')
        webbrowser.open('https://www.hotstar.com/in')
    elif 'prime' in query:
        Speak('opening your amazon prime videos')
        webbrowser.open('https://www.primevideo.com/')
    elif 'netflix' in query:
        Speak('opening Netflix videos')
        webbrowser.open('https://www.netflix.com/')
    else :
        No_result_found()

def temperature(query):
    IP_Address = get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    city = geo_data['city']
    search = f"temperature in {city}"
    url_1 = f"https://www.google.com/search?q={search}"
    r = get(url_1)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    Speak(f"current {search} is {temp}")

# Mail verification
def verifyMail():
    try:
        Speak("what should I say?")
        content = takecommand()
        to = d
        SendEmail(to, content)
        Speak("Email has been sent to " + str(to))
    except Exception as e:
        print(e)
        Speak("Sorry sir I am not not able to send this email")

    # Email Sender
def SendEmail(to, content):
    print(content)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(g, p)
    server.sendmail(g, to, content)
    server.close()


def No_result_found():
    Speak("Sir I couldn\'t understand, could you please say it again.")

def TaskExe():

    Speak("I am jarvis Sir, please tell me how can i help you ?")
    while True:
         query = takecommand()
         if 'hello' in query:
             Speak("Hello Sir")

         elif 'how are you' in query:
             Speak("I am fine Sir.")

         elif (('hi' in query) and len(query)==2) or ((('hai' in query) or ('hey' in query)) and len(query)==3) or (('hello' in query) and len(query)==5):
             comum(query)

         elif ('your age' in query) or ('are you single' in query) or (
                 'are you there' in query) or ('tell me something' in query) or (
                 'thank you' in query) or ('in your free time' in query) or (
                 'i love you' in query) or ('can you hear me' in query) or (
                 'do you ever get tired' in query):
             Fun(query)

         elif ('what can you do' in query) or ('your name' in query) or ('my name' in query) or ('university name' in query):
             Fun(query)

         elif ("goodbye" in query) or ("get lost" in query):
            Speak("Thanks for using me boss, have a good day")
            exit()

         elif ("college time table" in query) or ("schedule" in query):
            shedule()

         elif ("wake up" in query) or ("get up" in query):
            Speak("boss, I am not sleeping, I am in online, what can I do for u")

         elif 'you need a break' in query:
             Speak("Ok sir, you can call me anytime!")
             break

         elif ('system condition' in query) or ('condition of the system' in query):
            Speak("checking the system condition")
            condition()

         elif ('where i am' in query) or ('where we are' in query):
            locaiton()

         elif ('hotstar' in query) or ('prime' in query) or ('netflix' in query):
             OTT(query)

         elif "temperature" in query:
            temperature(query)

         elif ('silence' in query) or ('silent' in query) or ('keep quiet' in query) or ('wait for' in query):
             silenceTime(query)

         elif 'send email' in query:
             verifyMail()

         elif 'youtube search' in query:
             Speak("Ok Sir, This is what i found for your search!")
             query = query.replace("jarvis", "")
             query = query.replace("youtube search", "")
             web = "https://www.youtube.com/results?search_query=" + query
             webbrowser.open(web)

         elif 'google search' in query:
             Speak('This is what i found for your search sir!')
             query = query.replace("jarvis","")
             query = query.replace("google search","")
             pywhatkit.search(query)
             Speak("Done Sir")

         elif 'website' in query:
             Speak("Ok sir, Launching ....")
             query = query.replace("jarvis","")
             query = query.replace("website","")
             query = query.replace("open","")
             web2 = 'http://www.'+query+'.com'
             webbrowser.open(web2)
             Speak("Launched...!")

         elif 'launch' in query:
             Speak("Tell me the Name of website.")
             name = takecommand()
             web = 'https://'+name+'.com'
             webbrowser.open(web)
             Speak('done sir')

         elif 'play video song' in query :
             query = query.replace("play","")
             music()

         elif 'time' in query or "what's the time ":
             Clock_time(query)

         elif 'good morning jarvis' in query or 'good afternoon jarvis' in query or 'good evening jarvis' in query:
             wishMe()

         elif 'open' in query:
             openApps(query)

         elif 'wikipedia' in query:
             Speak("Searching wikipedia....")
             query = query.replace("jarvis",'')
             query = query.replace("wikipedia","")
             wiki = wikipedia.summary(query,2)
             Speak(f"According to wikipedia : {wiki})")

         elif 'open stackoverflow' in query:
             Speak("ok sir i will open the stck over flow website")
             webbrowser.open("https://wwww.stackoverflow.com")

         elif 'dictionary' in query:
             Dict()

         elif 'joke' in query or 'tell me a joke'in query or 'one more joke' in query:
             get = pyjokes.get_joke()
             Speak(get)

         elif 'repeat my words' in query:
             Speak("Speak sir !")
             jj = takecommand()
             Speak(f"You said :{jj}")

         elif ("today" in query) or ("What's the day" in query):
             day = Cal_day()
             Speak("Today is "+day)

         elif 'pause' in query:
             keyboard.press('space bar')

         elif 'close' in query:
             keyboard.press_and_release('command + w')

         elif 'restart' in query:
             keyboard.press('0')

         elif 'mute' in query:
             keyboard.press('m')

         elif 'skip' in query:
             keyboard.press('l')

         elif 'back ' in query:
             keyboard.press('j')

         elif 'full screen' in query:
             keyboard.press('f')

         elif 'film mode' in query:
             keyboard.press('t')

         elif 'open new tab' in query or 'new tab' in query or 'another tab' in query:
             keyboard.press_and_release('command + t')

         elif 'open new window' in query or 'new window' in query or 'another window' in query:
             keyboard.press_and_release('command + n')

         elif 'history' in query or 'open history' in query or 'show history' in query:
             keyboard.press_and_release('command + y')

         elif ('facebook' in query) or ('whatsapp' in query) or ('instagram' in query) or ('twitter' in query) or ('discord' in query) or ('social media' in query):
             social(query)

         elif ('instagram profile' in query) or("profile on instagram" in query):
             Instagram_Pro()

         elif 'whatsapp message' in query:
             query = query.replace("jarvis","")
             query = query.replace("send","")
             query = query.replace("whatsapp message","")
             query = query.replace("to","")
             name = query
             if 'pranav' in name:
                 numb= "8459651472"
                 Speak(f"What's the message for {name}")
                 mess = takecommand()
                 Whatsapp.whatsapp(numb,mess)

             elif 'rajat' in name:
                 numb = '8412013613'
                 Speak(f"What's the message for {name}")
                 mess = takecommand()
                 Whatsapp.whatsapp(numb, mess)

             elif 'yash' in name:
                 numb = '9325508332'
                 Speak(f"What's the message for {name}")
                 mess = takecommand()
                 Whatsapp.whatsapp(numb, mess)

             elif 'pujari' in name:
                 numb = '7057228375'
                 Speak(f"What's the message for {name}")
                 mess = takecommand()
                 Whatsapp.whatsapp(numb, mess)
         else:
             No_result_found()
TaskExe()


