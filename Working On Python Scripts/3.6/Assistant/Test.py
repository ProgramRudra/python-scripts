import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS
import requests, json
from playsound import playsound
import webbrowser
import socket
#Listen Function uses Microphone
def listen():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = recognize.listen(source)
    input = ""
    try:
        input = recognize.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return input
#Respond makes an audio file then plays it with responce
def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    playsound('speech.mp3')
def digital_assistant(input):
    global listening
    if "hello" in input:
        listening = True
        respond("hi")
    if "how are you" in input:
        listening = True
        respond("I am well")
    if "where do you live" in input:
        listening = True
        respond("In your computer")
    if "who created you" in input:
        listening = True
        respond("My creator is Rudra")
    if "What do you do" in input:
        listening = True
        respond("I am a Digital Assistant, I answer your questions")
    if "How old are you" in input:
        listening = True
        respond("I dont have an age")
    if "Are you a boy" in input:
        listening = True
        respond("I am a Assistant")
    if "what time is it" in input:
        listening = True
        respond("The time is " + ctime())

    #if "Search google for" in input:
    #    listening = True
    #    respond("Processing Query")
    #    input = input.split(" ")
    #    gurl = 'https://www.google.com/search?q='
    #    full = gurl + str(input[3])
    #    respond("Searching Now")
    #    webbrowser.open(full)
    if "send an email" in input:
        listening = True
        webbrowser.open('mailto:?')
    if "open" in input:
        listening = True
        respond("Locating Application")
        input = input.split(" ")
        os.system('open /Applications/'+str(input[1])+'.app')
        respond('I have Opened '+str(input[1]))
    if "what is my IP" in input:
        listening = True
        respond("Connecting to your server")
        ip = socket.gethostbyname(socket.gethostname())
        respond('Your IP Address is '+str(ip))
    if "where is" in input:
        listening = True
        input = input.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(input[2])
        respond("Hold on Rudra, I will show you where " + input[2] + " is.")
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)
        
    if "what is the weather in" in input:
        listening = True
        api_key = "c3af396cfdb21688d63a86a8de1d84dd"
        weather_url = "http://api.openweathermap.org/data/2.5/weather?q="
        input = input.split(" ")
        location = str(input[5])
        url = weather_url + location + "&appid=" + api_key
        js = requests.get(url).json() 
        if js['cod'] != "404":
            weather1 = js['main']
            temp = weather1['temp']
            hum = weather1['humidity']
            desc = js['weather'][0]['description']
            cel = int(temp) - 273.15
            far = (cel * 9/5)+32
            far = str(far).split(".")
            far2 = far[0]
            resp_string = "Here is the weather info for "+input[5]+ " The temperature in Fahrenheit is approximately " + str(far2) + ", The humidity is " + str(hum) + " and The weather description is "+ str(desc)
            respond(resp_string)
        else: 
            respond("City Not Found")
    if "search tik tok for" in input:
        listening = True
        tikurl = 'https://www.tiktok.com/search?q='
        fulltikurl = tikurl+str(input[3])
        opentik = '/usr/bin/open -a "/Applications/Safari.app"'+fulltikurl
        os.system(opentik)
        respond('Connecting to Tik Tok Server')
    if "shutdown my computer" in input:
        listening =True
        os.system('shutdown -h now')
    if "stop listening" in input:
        listening = False
        print('Listening stopped')
    return listening


respond("Hi Rudra, what can I do for you?")
listening = True
while listening == True:
    input = listen()
    listening = digital_assistant(input)
