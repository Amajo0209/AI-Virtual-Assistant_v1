import pyttsx3
import datetime
import speech_recognition as sr
import os
import serial
import time
#import schedule
import webbrowser as wb
import pause
import wikipedia
#from googletrans import Translator
import cv2
import numpy as np


# LIST OFF VARIABLES
board = 'COM4'
baud = 9600
name = 'lisa'
myName = 'name'
userName = 'joseph'
current_time = 'time'
greet = 'how are you'
glad = 'thanks'
music = 'song'
note = 'remember'
content = 'note'
lampON = 'on the lamp'
lampOFF = 'off the lamp'
doorON = 'open the door'
doorOFF = 'close the door'
AcON = 'on the air conditioner'
AcOFF = 'off the air conditioner'
offline = 'offline'
temp = 'temperature'
locate = 'where is'
wait = 'stop listening'
intro = 'yourself'
wik = "wikipedia"
awake = "awake"
translate = "translate this"
playlist = 'playlist'
miss = 'miss you'
plan = 'something'
morning = 'good morning'
noon = 'good afternoon'
evening = 'good evening'
wake = "hello lisa"
song = 'song'
cam = 'the camera'
det = 'face detection'
yout = 'youtube'
china = 'chinese'


ser = serial.Serial(board, baud)#Initializing the Serial Comunication
engine = pyttsx3.init()
#trans = Translator()

#OPENING THE WEBCAM

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


#Function for setting the Speak Properties
def speak(audio):
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 177)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)  
    engine.runAndWait()


#THIS FUNCTION ALLOWS THE USER TO SPEAK WITH THE AI
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-us')
        print(query)

    except Exception as e:
        print(e)
        return "none"
    return query.lower()


# FUNCTION THAT MAKES THE AI TO GREET THE USER ACCORDING TO TIME-PERIOD
def wishme():
    speak("starting all systems applications!")
    pause.seconds(2)
    speak("Setting up the Speech Recognition!")
    pause.seconds(2)
    speak("the speech recognition is ready!")
    speak("Establishing the connection with the Arduino board! Please, wait a moment!")
    pause.seconds(5)
    speak("the connection has been established!")
    speak("Hello! my name is LISA!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning" + userName)
    elif hour >= 12 and hour <= 18:
        speak("good afternoon " + userName)
    elif hour >= 18 and hour <= 24:
        speak("good evening" + userName)
    else:
        speak("good night" + userName)
    

# FUNCTION TO SPEAK THE TIME
def _time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("the current time is:")
    speak(Time)


def webcam():
    ret, frame = cap.read()
    cv2.imshow("LISA_CAM",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()

        
def commands():

    

    print("Listening...")

    query = takeCommand()

    if query.count(wake) > 0:
            speak("yes Joseph! How may I help you?")
            query = takeCommand()

            if current_time in query:
                _time()
            elif greet in query:
                speak("Im good! Thanks for asking")
                speak("is there anything that I can do for you?" + userName)
            elif awake in query:
                speak("yes"+userName+"! is there anything I can do for you?")
            elif wait in query:
                speak("for how many minutes you want me to stop listening?")
                ans = int(takeCommand())
                speak("you told me to stop listening to your commands for:" + str(ans)+"minutes")
                pause.minutes(ans)
                speak("I'm back" + userName)

            elif miss in query:
                speak("I missed you too " + userName + "!"+"you've been such a cool guy!")
                speak("Now! tell me how can I help you!")
            elif plan in query:
                speak("you look so excited " + userName)
                speak("that's really great!")
            elif china in query:
                engine.say("你好")

            #PLAYING SONGS
            elif song in query:
                speak("what do you want me to play?")
                query = takeCommand()
                if playlist in query:
                    speak("Okay " + userName)
                    songs_dir = 'D:\Music'
                    songs = os.listdir(songs_dir)
                    os.startfile(os.path.join(songs_dir, songs[0]))
                elif 'any song' in query:
                    songs_dir = 'D:\Music01\Moise Mbiye'
                    songs = os.listdir(songs_dir)
                    os.startfile(os.path.join(songs_dir, songs[0]))
                    
            #GREETING
            elif morning in query:
                hour = datetime.datetime.now().hour
                if hour >= 6 and hour <= 12:
                    speak("Good morning" + userName)
                    speak("What can I do for you?")
                    takeCommand()
                elif hour >= 12 and hour <= 18:
                    speak("now is afternoon!")
                    speak("good afternoon " + userName)
                elif hour >= 18 and hour <= 24:
                    speak("now is evening")
                    speak("good evening" + userName)
                else:
                    speak("good night" + userName)

            elif noon in query:
                hour = datetime.datetime.now().hour
                if hour >= 6 and hour <= 12:
                    speak("now is morning!")
                    speak("Good morning" + userName)
                elif hour >= 12 and hour <= 18:
                    speak("good afternoon " + userName)
                    speak("What can I do for you?")
                    takeCommand()
                elif hour >= 18 and hour <= 24:
                    speak("now is evening")
                    speak("good evening" + userName)
                else:
                    speak("good night" + userName)

            elif evening in query:
                hour = datetime.datetime.now().hour
                if hour >= 6 and hour <= 12:
                    speak("now is morning!")
                    speak("Good morning" + userName)
                elif hour >= 12 and hour <= 18:
                    speak("now is afternoon!")
                    speak("good afternoon " + userName)
                elif hour >= 18 and hour <= 24:
                    speak("good evening" + userName)
                    speak("What can I do for you?")
                    takeCommand()
                else:
                    speak("good night" + userName) 
                
            #SELF-INTRODUCTION AND REMEMBER
            elif note in query:
                speak("what do you want me to remember?")
                data = takeCommand()
                speak("you told me to remember " + data)
                remember = open("data.txt", "w")
                remember.write(data)
                remember.close()
            elif content in query:
                remember = open("data.txt", "r")
                speak("Yes" + userName)
                speak("you told me to remember " + remember.read())
            elif myName in query:
                speak(" Your name is " + userName + "sir!")
            elif intro in query:
                speak("My name is LISA! I'm a personal assistant created by Joseph Dream. He created me to help him with some tasks. I can perform tasks like playing songs, searching the internet, locating places, but the most important is, I can control any appliance connected to boards such as Arduino, ESP, Rasberry Pi.")

            # LOCATION FUNCTION
            elif locate in query:
                query = query.replace(locate, "")
                location = query
                speak(userName + "you asked me to locate" + location)
                wb.open_new_tab("https://www.google.com/maps/" + location)

            #SEARCHING THE INTERNET FUNCTION  
            elif wik in query:
                speak("what do you want me to search?")
                query = takeCommand()
                speak("Alright " + userName + "wait a minute!")
                query = query.replace(wik,"")
                result = wikipedia.summary(query,sentences=3)
                print(result)
                speak(result)
            
            elif yout in query:
                speak("What do you want to watch?")
                topic = takeCommand()
               # pywhatkit.playonyt(topic)
            
            elif det in query:
                speak("Starting face detection " + userName)
                webcam()
                

            # CONTROLLING LAMPS
            elif lampON in query:
                ser.write(b'A')
                speak("turning on the Lamp" + userName)
                query = takeCommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")

            elif lampOFF in query:
                ser.write(b'a')
                speak("OKAY" + userName + '!' + "turning off the lamp!")
                query = takeCommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")


            # Controlling the door
            elif doorON in query:
                ser.write(b'B')
                speak("alright" + userName + "the door is opened!")
                query = takeCommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")

            elif doorOFF in query:
                ser.write(b'b')
                speak("okay" + userName + 'closing the door!')
                query = takeCommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")

            # Cotrolling the Air Conditioner
            elif AcON in query:
                ser.write(b'C')
                speak("switching on the air conditioner!")
                query = takeCommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")
            elif AcOFF in query:
                ser.write(b'c')
                speak("Switching off the Air conditioner" + userName)
                query = takeCommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")
                

            # ASKING LISA TO READ DATA FROM DHT11
            elif temp in query:
                if ser.in_waiting > 0:
                    rawserial = ser.readline()
                    cookedserial = rawserial.decode('utf-8').strip('\r\n')
                    datasplit = cookedserial.split(',')
                    temperature = datasplit[0].strip('<')
                    humidity = datasplit[1].strip('>')
                    speak("the sensor is registring a temperature of " + temperature + "degrees Celcius!" + "and a humidity of" + humidity + "percent")
            
                        

            # ASKING LISA TO STAY OFFLINE
            elif offline in query:
                speak("See you next time Joseph!")
                quit()


    elif name in query:
        if current_time in query:
                _time()
        elif greet in query:
            speak("Im good! Thanks for asking")
            speak("is there anything that I can do for you?" + userName)
        elif awake in query:
            speak("yes"+userName+"! is there anything I can do for you?")
        elif wait in query:
            speak("for how many minutes you want me to stop listening?")
            ans = int(takeCommand())
            speak("you told me to stop listening to your commands for:" + str(ans)+"minutes")
            pause.minutes(ans)
            speak("I'm back" + userName)

        elif miss in query:
            speak("I missed you too " + userName + "!"+"you've been such a cool guy!")
            speak("Now! tell me how can I help you!")
        elif plan in query:
            speak("you look so excited " + userName)
            speak("that's really great!")

        #PLAYING SONGS
        elif song in query:
            speak("what do you want me to play?")
            query = takeCommand()
        if playlist in query:
            speak("Okay " + userName)
            songs_dir = 'D:\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'any song' in query:
            songs_dir = 'D:\Music01\Moise Mbiye'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
                        
        #GREETING
        elif morning in query:
            hour = datetime.datetime.now().hour
            if hour >= 6 and hour <= 12:
                speak("Good morning" + userName)
                speak("What can I do for you?")
            elif hour >= 12 and hour <= 18:
                speak("now is afternoon!")
                speak("good afternoon " + userName)
            elif hour >= 18 and hour <= 24:
                speak("now is evening")
                speak("good evening" + userName)
            else:
                speak("good night" + userName)

        elif noon in query:
            hour = datetime.datetime.now().hour
            if hour >= 6 and hour <= 12:
                speak("now is morning!")
                speak("Good morning" + userName)
            elif hour >= 12 and hour <= 18:
                speak("good afternoon " + userName)
                speak("What can I do for you?")
            elif hour >= 18 and hour <= 24:
                speak("now is evening")
                speak("good evening" + userName)
            else:
                speak("good night" + userName)

        elif evening in query:
            hour = datetime.datetime.now().hour
            if hour >= 6 and hour <= 12:
                speak("now is morning!")
                speak("Good morning" + userName)
            elif hour >= 12 and hour <= 18:
                speak("now is afternoon!")
                speak("good afternoon " + userName)
            elif hour >= 18 and hour <= 24:
                speak("good evening" + userName)
                speak("What can I do for you?")
            else:
                speak("good night" + userName) 
                    
        #SELF-INTRODUCTION AND REMEMBER
        elif note in query:
            speak("what do you want me to remember?")
            data = takeCommand()
            speak("you told me to remember " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif content in query:
            remember = open("data.txt", "r")
            speak("Yes" + userName)
            speak("you told me to remember " + remember.read())
        elif myName in query:
            speak(" Your name is " + userName + "sir!")
        elif intro in query:
            speak("My name is LISA! I'm a personal assistant created by Joseph Dream. He created me to help him with some tasks. I can perform tasks like playing songs, searching the internet, locating places, but the most important is, I can control any appliance connected to boards such as Arduino, ESP, Rasberry Pi.")

        # LOCATION FUNCTION
        elif locate in query:
            query = query.replace(locate, "")
            location = query
            speak(userName + "you asked me to locate" + location)
            wb.open_new_tab("https://www.google.com/maps/" + location)

        #SEARCHING THE INTERNET FUNCTION  
        elif wik in query:
            speak("what do you want me to search?")
            query = takeCommand()
            speak("Alright " + userName + "wait a minute!")          
            query = query.replace(wik,"")
            result = wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)
                
        elif yout in query:
            speak("What do you want to watch?")
            topic = takeCommand()
            # pywhatkit.playonyt(topic)

                
        elif det in query:
            speak("Starting face detection " + userName)
            webcam()
                    

        # CONTROLLING LAMPS
        elif lampON in query:
            ser.write(b'A')
            speak("turning on the Lamp" + userName)
            query = takeCommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")

        elif lampOFF in query:
            ser.write(b'a')
            speak("OKAY" + userName + '!' + "turning off the lamp!")
            query = takeCommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")


        # Controlling the door
        elif doorON in query:
            ser.write(b'B')
            speak("alright" + userName + "the door is opened!")
            query = takeCommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")

        elif doorOFF in query:
            ser.write(b'b')
            speak("okay" + userName + 'closing the door!')
            query = takeCommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")

        # Cotrolling the Air Conditioner
        elif AcON in query:
            ser.write(b'C')
            speak("switching on the air conditioner!")
            query = takeCommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
        elif AcOFF in query:
            ser.write(b'c')
            speak("Switching off the Air conditioner" + userName)
            query = takeCommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
                    

        # ASKING LISA TO READ DATA FROM DHT11
        elif temp in query:
            if ser.in_waiting > 0:
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                datasplit = cookedserial.split(',')
                temperature = datasplit[0].strip('<')
                humidity = datasplit[1].strip('>')
                speak("the sensor is registring a temperature of " + temperature + "degrees Celcius!" + "and a humidity of" + humidity + "percent")
                
                            

        # ASKING LISA TO STAY OFFLINE
        elif offline in query:
            speak("See you next time Joseph!")
            quit()



if __name__ == "__main__":

    wishme()

    while True:
        commands()
