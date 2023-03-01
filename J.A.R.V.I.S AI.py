#import libraries
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os
import smtplib

#set voice in speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#function for speech of code
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function for wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

#user voice command input function
def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")
        typeInstead()
        return "None"
    return query

#if voice not accepting, function for that
def typeInstead():
    speak("Please type you input")
    query = input(str("Please type your input instead: "))
    if query == "no":
        print("Ok. Thanks for your time")
        speak("Ok. Thanks for your time")

#function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


#main loop
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # use you own music directory/ file location while running it
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "E:\Study Miscellaneous\Python Programming\VS Codes - Python\Completed Projects for GITHUB\J.A.R.V.I.S AI.py"
            #use your own file location/directory while running it
            os.startfile(codePath)
            
        elif 'spotify' in query:
            webbrowser.open('spotify')
            
        elif 'date' in query:
            strDate =datetime.datetime.now().strftime("%d")

        elif 'mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mail@gmail.com"    
                #use your own email, i have reemoved mine
                sendEmail(to, content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
                
        elif 'exit' in query:
            print("THANK YOU FOR USING ME")
            speak("Thank you for your Time")
            break
        
        
        
        else:
            print("NO DATA FOUND !!!")
            speak(f"I have no data with the name {query}")
