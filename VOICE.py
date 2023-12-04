from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import random
import time
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")
 
    speak("Ready To Comply. What can I do for you ?")

def takeCommand():
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
        print("Say that again please...")
        # speak('could you repeat sir?') 
        return "None"
    return query.lower().strip()
def get_joke():
            jokes = [
        "Why don't scientists trust atoms? Because they make up everything! HA HA HA HA HA",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them! HA HA HA HA HA",
        "Why did the scarecrow win an award? Because he was outstanding in his field! HA HA HA HA HA",
        "What do you call fake spaghetti? An impasta! HA HA HA HA HA",
        "Why don't oysters donate to charity? Because they are shellfish! HA HA HA HA HA",
        "What do you call a fish with no eyes? Fsh! HA HA HA HA HA",
        "Why did the coffee file a police report? It got mugged! HA HA HA HA HA",
        "How do you organize a space party? You planet! HA HA HA HA HA",
        "Why did the bicycle fall over? Because it was two-tired! HA HA HA HA HA",
        "What's a vampire's favorite fruit? A blood orange! HA HA HA HA HA",
        "Why did the math book look sad? Because it had too many problems! HA HA HA HA HA",
        "What did one hat say to the other? Stay here, I'm going on ahead! HA HA HA HA HA",
        "How do you catch a squirrel? Climb a tree and act like a nut! HA HA HA HA HA",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field! HA HA HA HA HA"
        ]
            return random.choice(jokes)
def open_netflix():

    driver_path = '/path/to/chromedriver'


    driver = webdriver.Chrome(executable_path=driver_path)


    driver.get("https://www.netflix.com")
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:        
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that topic.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are multiple possible matches. Please specify: {e.options}")
        elif any(keyword in query for keyword in ['who are you', 'what is your name', 'introduce yourself']):
            print('My Name Is HELAPP')
            speak('My Name Is HELAP')
            print('I am a virtual assistant that can to whatever you would like me to do')
            speak('I am a virtual assistant that can to whatever you would like me to do. For example: telling the jokes, calculate, open different apps')
        elif any(keyword in query for keyword in ['who is your creator', 'who created you', 'tell me about your creator']):
            print('I was created by the group members of the project to assist and help disabled people')
            speak('I was created by the group members of the project to assist and help disabled people')
# -----------------------------------------------------------------------------------------------------------------            
        elif any(keyword in query for keyword in ['search on youtube','youtube search']):
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
# -----------------------------------------------------------------------------------------------------------------            
        elif 'open youtube' in query:
            speak("what we gonna watch sir?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")
        elif 'close youtube' in query:
            pyautogui.hotkey('ctrl', 'w')
# -----------------------------------------------------------------------------------------------------------------            
        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            speak('in process sir')
            webbrowser.open('https://www.google.com/search?q=' + qry)
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif any(keyword in query for keyword in ['open tab','open new tab']):
            pyautogui.hotkey('ctrl', 't')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close google' in query:
            os.system("taskkill /f /im chrome.exe")
        elif any(keyword in query for keyword in ['play music','open spotify', 'open music']):
            music_dir = "D:\Новая папка\Spotify.lnk"
            os.startfile(music_dir)
        elif any(keyword in query for keyword in ['close music','stop music', 'close spotify']):
            os.system("taskkill /f /im spotify.exe")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:") 
            speak(f"Sir, the time is {strTime}")
# ----------------------------------------------------------------------------------------------------------------------------
        elif "open notepad" in query:
            npath = r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2310.13.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe"
            os.startfile(npath)
        elif "close notepad" in query:
            os.system('taskkill /f /im Notepad.exe')
        elif any(keyword in query for keyword in ['open telegram','telegram']):
            tpath = r"C:\Program Files\WindowsApps\TelegramMessengerLLP.TelegramDesktop_4.11.8.0_x64__t4vj0pshhgkwm\Telegram.exe"
            os.startfile()
        elif any(keyword in query for keyword in ['close telegram']):
            os.system('taskkill /f /im TelegramDesktop.exe')
        elif any(keyword in query for keyword in ['open visual code studio']):
            vcode_path = r"C:\Users\meder.ymanaliev\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(vcode_path)
        elif any(keyword in query for keyword in ['close visual code studio']):
            os.system('taskkill /f /im Code.exe')
        elif any(keyword in query for keyword in ['open whatsapp','whatsapp']):
            wppath = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2347.1.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
        elif any (keyword in query for keyword in ['close whatsapp']):
            os.system('taskkill /f /im WhatsApp.exe')
        elif any (keyword in query for keyword in ['open netflix',' netflix']):
            
            
            pass
        elif "take screenshot" in query:
            speak('tell me a name for the file to save')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot() 
            img.save(f"{name}.png") 
            speak("screenshot saved")
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    '/' : operator.__truediv__,}[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = float(op1), float(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        elif any(keyword in query for keyword in ['what is my ip address','tell me my ip address','ip address']):
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif any(keyword in query for keyword in['go to sleep', 'stop listening', 'you can rest', 'good bye', "you did a good job"]):
            speak('alright then, I am switching off')
            sys.exit()
        elif "refresh" in query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=556, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        elif "scroll down" in query:
            pyautogui.scroll(700)
        elif "scroll up" in query:
            pyautogui.scroll(-700)
        elif any(keyword in query for keyword in ['thank you','thank you very much','thanks']):
            speak('always at your service sir.')
            print('always at your service sir.')
        elif any(keyword in query for keyword in ['roll down all the windows','down all the windows']):
            pyautogui.hotkey('win', 'd')
        elif any(keyword in query for keyword in['roll up the last window', 'roll up the previous window']):
            pyautogui.hotkey('alt', 'tab')
        elif any(keyword in query for keyword in ['I am sad', 'tell me a joke', 'joke']):
            joke = get_joke()
            speak(joke)
        elif 'shut down the system' in query:
            confirmation = input("Are you sure you want to shut down the system? (yes/no): ").lower()
            if confirmation == 'yes':
                speak("Shutting down the system. Goodbye!")
                os.system("shutdown /s /t 5")
            else:
                speak("Shutdown canceled. Resuming normal operation.")

        elif "restart the system" in query:
            confirmation = input("Are you sure you want to shut down the system? (yes/no): ").lower()
            if confirmation == 'yes':
                speak("Shutting down the system. Goodbye!")
                os.system("shutdown /r /t 5")
            else:
                speak("Shutdown canceled. Resuming normal operation.")
        elif "lock the system" in query:
            time.sleep(5)
            speak('computer will go to sleep in 5 seconds')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            




                    


        














