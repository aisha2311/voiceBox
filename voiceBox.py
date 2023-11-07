from ast import operator
import profile
from urllib import request
import pyttsx3 # converting voice into text 
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit  
import sys   
import time    
#import pyjoke
import pyautogui
import operator
from bs4 import BeautifulSoup
import psutil




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




#convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1 
        audio=r.listen(source)

    try:
        print("reconizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    query=query.lower()
    return query
# def weather():
#     try:
#         speak("Checking the details for weather...")
#         URL = "https://weather.com/weather/today/l/26.62,87.36?par=google&temp=c"
#         header = {"User-Agent":'your user agent'}
#         page = requests.get(URL, headers=header)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         temperature = soup.find(class_="CurrentConditions--tempValue--3KcTQ").get_text()
#         description = soup.find(class_="CurrentConditions--phraseValue--2xXSr").get_text()
#         temp = "Sir, the temperature is " + temperature + " celcius." + ' and it is ' + description + ' outside.'
#         speak(temp)
#         if temperature < '20°':
#             speak("It will be better if you wear woolen clothes, sir.")
#         elif temperature <= '14°':
#             speak("Sir, it is very cold outside. If you want to go outside, wear woolen clothes.")
#         elif temperature >= '25°':
#             speak("Sir, you donot need to wear woolen clothes to go outside.")
#     except Exception as e:
#         speak("I am sorry due to technical issue i get feath current weather")

def battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    speak(f"Sir, it is {battery_percentage} percent.")
    if plugged:
        speak("and It is charging....")
    if not plugged:
        if battery_percentage <= "95%":
            speak("Sir, plug charger.")

def wishMe():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M%p")
    if hour>=0 and hour<12:
        speak(f"good Morning , its {tt}")
    elif hour>=12 and hour<18:
        speak(f"good afternoon , its {tt}")
    else:
        speak(f"good Evening ,its {tt}")
    speak("I am akira please tell me how can i help you")

# news function
def news():

    main_url="http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c4704c91a8d14871925651546267afdd"
    main_page=requests.get(main_url).json()
    #print (main_page)
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","forth","fifth","sixth","seventh","eighth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is:{head[i]}")

def click():
    pyautogui.click()


def username():
    username = psutil.users()
    for user_name in username:
        first_name = user_name[0]
        speak(f"Sir, this computer is signed to {first_name} as a username.")

if _name=="main_":

    wishMe()
    while True:

    #if 1:
        query=takecommand()

        if "how are you" in query:
            speak("i am fine sir what about you")
        
        # elif "who are you" in query:
        #     speak("I am a bot and your assistant named akira ")

        elif 'open code'in query:

            codePath="C:\\Users\\ashiu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "close code" in query:
            speak("ok sir, closing code")
            os.system("taskkill/f/im Code.exe")


        elif"who are you" in query:
            speak("i am akira , i am voice control assistent i can play audio control your pc answer your simple question ")

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif "open camera" in query:
            try:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break
                    cap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                speak("switch on the camera")

        elif 'click the mouse' in query or 'click mouse' in query or 'click' in query:
            click()
            

        elif 'battery percentage' in query or 'percentage in battery' in query or 'percent in my pc' in query:
            battery()


        # elif "play music" in query:
        #     music_dir="file name"
        #     songs=os.listdir()
        #     os.songs=os.listdir(music_dir)
        #     rd=random.choice(songs)
        # //for song in songs:
        #    // if song.endwith('.mp3'):
        #        // os.startfile(os.path.join(music_dir,song))

        #     os.startfile(os.path.join(music_dir,rd))


        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")


        elif "wikipedia" in query:
            
            speak("searching wikipedia...")
            try:
                query=query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia ")
                speak(results)
            except Exception as e:
                speak("please say it again in format of wikipedia virat or something like this")
        
        elif 'open map' in query or 'show my location' in query:
            webbrowser.open("https://www.google.com/maps/@26.6235458,87.3614451,16z")
            speak("Opening Maps...")

        elif"open youtube"  in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube....")

        elif "close youtube" in query:
            pyautogui.hotkey('ctrl', 'w')
            speak(" Youtube closed")

        elif "thank you" in query:
            speak("Its my pleasure sir")
        
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query or "mute volume" in query:
            pyautogui.press("mute")

        elif "scroll down" in query:
            speed=-30
            sleep=4
            pyautogui.time.sleep(2)
            pyautogui.scroll(speed)
            pyautogui.time.sleep(2)
            speak("scroll down successfull")
            
        


        elif"open facebook" in query:
            webbrowser.open("facebook.com")
        
        elif"open insta" in query:
            webbrowser.open("instagram.com")
            
        elif "close insta" in query:
            
            pyautogui.hotkey('ctrl', 'w')
            


        elif"open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif"open google" in query:
            speak("sir, what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "youtube search" in query:
            speak("sir, what should i search on youtube ")
            cm=takecommand().lower()
            webbrowser.open("https://www.youtube.com/results?search_query="+cm)

#update this method as google 
        # elif "send message" in query:

        #     kit.sendwhatmsg("+919128548336","this is test ",2,25)
        
        elif 'play' in query:
                try:
                    song=query.replace("play","")
                    speak("playing"+song)
                    pywhatkit.playonyt(song)
                except Exception as e:
                    speak("you don't have music in your file")
                

        
        elif 'close current window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            speak('Current window is closed.')

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        

        elif 'username' in query or 'user' in query or 'user name' in query:
            username()
        
 
        elif "tell me news" in query or "news " in query:
            speak("please wait sir, feteching the latest news")
            news()

        elif "where we are" in query or "where i am" in query:
            speak("wait sir, let me check")
            try:
                ipAdd=requests.get("https://api.ipify.org").text
                print(ipAdd)
                url="https://get.geojs.io/v1/ip/geo/"+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data["city"]
                country=geo_data["country"]
                speak(f"sir i am not sure, but i think we are in  {city} city of {country} country")
            except Exception as e:

                speak("sorry sir , due to some network issue i can't aable to locate us")


        elif " take screenshot" in query or "take a screenshot" in query:
            speak("sir , please tell me the name of this screenshot file")
            name=takecommand().lower()
            speak("please sir hold the screen for few second , i am taking screensort")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir the screenshot is saved in our main folder . now i am ready for next command")



        elif "instagram profile" in query or "profile on insta" in query:
            speak("sir please enter the user name correctly")
            name=input("enter user name correctly")
            webbrowser.open(f"www.instagram.com/{name}")
            #time.sleep(5)
            #speak("sir would you like to download profile picture of this account")
            # condition=takecommand().lower()
            # if "yes" in condition:
            #     mod=instaloader.Instaaloader() #pip instadownloader
            #     mod.download_profile(name,profile_pic_only=True)
            #     speak("i am done and dp has been save in your main folder now i am ready for next command")
            # else:
            #     pass



        elif "can you calculate " in query or "do some calculation" in query:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate , example : 3 pplus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+':operator.add,
                    '-':operator.sub,
                    'x':operator.mul,
                    'divided':operator._truediv_,
                }[op]
            def eval_binary(op1,oper,op2):
                op1,op2=int(op1),int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is ")
            speak(eval_binary(*(my_string.split())))
        



        






        elif "you can sleep"  in query:
            speak("thanks for using me sir, have a good  day")
            break
        
        
        elif "shutdown the system"  in query:
            os.system("shutdown/s/t 5")
        
        elif "restart the system" in query:
            os.system("restart/r/t 5")
            
        elif "sleep the system"in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        



            
        # elif "tell me a joke" in query:
        #     joke= pyjokes.get_joke()
        #     speak(joke)



        #speak("sir, do you have any other work")
        # elif "close code" in query:
        #     speak("ok sir, closing code")
        #     os.system("taskkill/f/im Code.exe")

# for alarm
        # '''elif "set alarm" in query:
        #     nn=int(datetime.datetime.now().hour)
        #     if nn==22:
        #         music_dir='filename'
        #         songs=os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir,song[0]))'''

    # while True:
        

    #     permission = takecommand()
        
    #     if " wake up " in permission:  
    #         speak("hello")
    #         TaskExecution()

    #     elif"goodbye" in permission:
    #         speak("have a nice day")
    #         sys.exit()