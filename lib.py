from importlib.resources import path
from unittest import result
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 166)


engine.setProperty('volume', 0.7)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def whishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")    


def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")

        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)


    try:
        print("Recognizing...")
        speak("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)

        print("Say that again...")
        speak("Say that again...")
        return "None"
    return query




    
    
if __name__ == '_main_':
    whishMe()
   

    speak("I Am Vision, How may I help you?")


while True:
    query = takeCommand().lower()
   
   
    if 'washroom' in query:
        engine.say('It is present at each floor, for gents, left side at end, for ladies, right side at end')
        speak("would you like to know anything else, or say exit")


#Ground Flooor
 
    elif 'seminar' in query:
       speak("It is at ground floor, move towards right exit of the reception hall, room number G 115")
       speak("would you like to know anything else, or say exit")


    elif 'department of student affair' in query:
        speak("It is at ground floor, move towards right exit of the reception hall, next to the seminar hall, room number G 114")
   
   
    elif 'library' in query:
        speak('It is at the ground floor, move towards right exit of the reception, next to the DSA room, room number G 113')
        speak("would you like to know anything else, or say exit")



    elif 'office' in query:
       speak("It is at ground floor, move towards left exit of the reception hall and then take left, room number G 101 ")
       speak("would you like to know anything else, or say exit")



    elif 'director' in query:
        speak("It is at ground floor, move towards left exit of the reception hall and then take left, room number G 110 ")
        speak("would you like to know anything else, or say exit")



    elif 'chairman' in query:
        speak("It is at ground floor, move towards left exit of the reception hall and then take right, room number G 111 ")
        speak("would you like to know anything else, or say exit")
        
        

    elif 'principal' in query:
        speak("It is at ground floor, move towards left exit of the reception hall and then take left, room number G 106 ")
        speak("would you like to know anything else, or say exit")
        
        

    elif 'examination' in query:
        speak("It is at ground floor, move towards left exit of the reception hall and then take left, room number G 102 ")
        speak("would you like to know anything else, or say exit")
        
        

    elif 'waiting room' in query:
        speak("It is at ground floor, move towards left exit of the reception hall and then take left, room number G 107 ")
        speak("would you like to know anything else, or say exit")
        
        
    elif 'department of electrical and electronic' in query:
        speak("It is at ground floor, move towards left exit of the reception hall and then take right, room number G 112 ")
        speak("would you like to know anything else, or say exit")
#First Floor



    elif 'placement cell' in query:
        speak("It is at first floor,then turn left, room number F 201 ")
        speak("would you like to know anything else, or say exit")


    elif 'i q a c office' in query:
        speak("It is at first floor,then turn right, room number F 207 ")
        speak("Would You like to know something else, if not then say exit.")





    elif 'digital library' in query:
        speak("It is at first floor,then turn right, room number F 208")
        speak("would you like to know anything else, or say exit")


    elif 'research innovation' in query:
        speak("It is at first floor,then turn right, room number F 209")
        speak("would you like to know anything else, or say exit")


    elif 'mechanical engineering' in query:
        speak("It is at first floor,then turn right, room number F 213")
        speak("would you like to know anything else, or say exit")

#Second Floor


    elif 'department of cse' in query:
        speak("It is at 3rd floor, you can use elevator or you can use stairs then, turn right, room number 309")
        speak("would you like to know anything else, or say exit")




    elif 'seed' in query:
        speak("It is at 3rd floor, you can use elevator or you can use stairs then, turn right, room number 310")
        speak("would you like to know anything else, or say exit")


    elif 'humanities and science' in query:
        speak("It is at 3rd floor, you can use elevator or you can use stairs then, turn left, room number 301")
        speak("would you like to know anything else, or say exit")


    elif 'hod cabin' in query:
        speak("It is at 3rd floor, you can use elevator or you can use stairs then, turn right, room number 311")
        speak("would you like to know anything else, or say exit")

#third floor



    elif 'educational technology' in query:
        speak("It is at 4th floor, you can use elevator or you can use stairs then, turn right, room number 309")
        speak(",,,,   would you like to know anything else, or say exit")


    elif 'exit' in query:
        speak("Thank you for visting")
        exit()




    else:
        speak('Information Not Available')
