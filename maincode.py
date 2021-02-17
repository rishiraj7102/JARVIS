import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from win10toast import ToastNotifier

import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):  # speaks the string passed
    engine.say(text)
    engine.runAndWait()


def wishme():  # wishes you according to the time
    h = int(datetime.datetime.now().hour)
    if (h >= 6) and (h < 12):
        speak("Good Morning Sir")
    elif (h >= 12) and (h < 18):
        speak("Good afternoon Sir")
    elif (h >= 18) and (h <= 19):
        speak("Good evening Sir")

   # speak('I am Jarvis. How may I help you Sir?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}\n")
    except Exception as e:
        print("I was unable to catch it. Could you please repeat")
        query = None
    return query


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailID@gmail.com', "yourPassword")
    server.sendmail('SenderEmailId@gmauil.com', to, content)
    server.close()


print("Initializing Jarvis")
speak("Initializing Jarvis")

wishme()
query = takecommand()

if 'Wikipedia' in query:
    speak('Searching Wikipedia')
    query = query.replace('wikipedia', " ")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif 'open YouTube' in query:  # opens YT on Chrome
    url = 'http://youtube.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open Reddit' in query:  # opens Reddit on Chrome
    url = 'http://reddit.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open Instagram' in query:  # opens Insta on Chrome
    url = 'http://instagram.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open GitHub' in query:  # opens GitHUb on Chrome
    url = 'http://github.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open Google' in query:  # opens Google
    url = 'http://google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open CodeChef' in query:  # opens Codechef on chrome
    url = 'http://codechef.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open LinkedIn' in query:  # opens Linkedin on chrome
    url = 'http://linkedin.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open Facebook' in query:  # opens Facebook on chrome
    url = 'http://facebook.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'play music' in query:  # plays the first music in the file
    songs_dir = 'C:\\Users\\RISHABH JAIN\\Music\\Video Projects'
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
elif 'hello' in query:    #responds to you when you say hello
    speak("Hello Sir. Nice to hear from you ")
elif 'my personal details' in query:   #tells me few small personal details
    speak("Your  name  is  Rishabh  Kamlesh  Jain.  Your  age  is  18  years  and  you  are  a  sophomore  at  VIT  Bhopal  University.  You  currently  are  studying  CSE   with  Artificial  Intelligence  and  Machine  Learning. Cant  disclose  more information  as  it  is  against  my  rules!")
elif 'alarm' in query:    #sets an alarm according to the time you want and shows a notification on windowss\
    speak("What hour do you want the alarm")
    hours = int(input())
    speak("What minute do you want the alarm")
    minutes = int(input())
    speak("Is it morning or evening")
    AmPm = takecommand()
    if 'evening' in AmPm:
        hours = hours + 12
    while True:
        if (hours == datetime.datetime.now().hour) and (minutes == datetime.datetime.now().minute):
            speak("SIR WAKE UP! ITS TIME !")
            toaster=ToastNotifier()
            toaster.show_toast("ALert!",'The timer is over ',threaded=True,icon_path=None,duration=10)
            wishme()
            break
elif 'time' in query:  # tells the present time
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir the time is {strTime}")
elif 'open Dev C plus plus' in query:  # opens Devc++
    codepath = 'C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'
    os.startfile(codepath)
elif 'open dev c++' in query:  # opens Devc++
    codepath = 'C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'
    os.startfile(codepath)
elif 'email' in query:  # pseudo email sender
    try:
        speak('What should I send')
        content = takecommand()
        to = "senderEmailId@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent Successfully")
    except Exception as e:
        print(e)
