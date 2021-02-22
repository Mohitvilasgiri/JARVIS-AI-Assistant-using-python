import pyttsx3
import random
import speech_recognition as sr  
import datetime  
import wikipedia
import webbrowser
import os          
from pyfirmata import Arduino, util    # importing Arduino Board from pyfirmata module
from pyfirmata import OUTPUT           # importing Output from pyfirmata module

"""
Now we will set our engine to Pyttsx3 which is used for text to speech in Python and sapi5 is 
Microsoft speech application platform interface we will be using this for text to speech function 
and getting details of current voice and changing index, changes voices. o for male.

"""

engine = pyttsx3.init('sapi5')        
voices = engine.getProperty('voices')  #getting details of current voice
engine.setProperty('voice', voices[0].id)


"""
Read and write the pins on the Arduino.
Here we select port of laptop and setting the pins as output and state there position as LOW (0)

"""
board = Arduino('COM6')
board.digital[10].mode =OUTPUT
board.digital[11].mode =OUTPUT
board.digital[12].mode =OUTPUT

board.digital[10].write(0)
board.digital[11].write(0)
board.digital[12].write(0)


"""
we create speak function which speaks our written string. wishme function wish according to the time and take command function use laptop
 microphone  to listen and recognized using recognize_google 


"""

def speak(audio):
	engine.say(audio)
	engine.runAndWait()     # Without this command, speech will not be audible to us.

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Hello, Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Hello, Good Afternoon Sir !") 

	else:
		speak("Hello, Good Evening Sir !") 

	assname =("Jarvis")
	speak("I am your Assistant")
	speak(assname)
	

def usrname():
	speak("How can i Help you, Sir")


def takeCommand():
	
    #It takes microphone input from the user and returns string output


	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')   #Using google for voice recognition.
		print(f"User said: {query}\n")        # User query will be printed .

	except Exception as e:
		print(e) 
        #speak("Unable to Recognize your voice")
		print("Unable to Recognize your voice.")    # Say that again will be printed in case of improper voice 
		return "None"       # None string will be returned
	
	return query

"""
Calling all the function & and make conditions (In main function).
We calling all the function which we define
And creating condition like open google, music, search, etc.


"""


if __name__ == '__main__':

    wishMe()
    usrname()
 
    while True:
         
        query = takeCommand().lower()  # Converting user query into lower case
         
         # Logic for executing tasks based on query

        if 'wikipedia' in query:     #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

		
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")   
 
        elif 'play music' in query:
            music_dir = r'C:\\Users\\MOHIT VILAS GIRI\\Desktop\\load\\mission\\New folder'
           
            songs =os.listdir(music_dir)
        
            random.shuffle(songs)
            os.startfile(os.path.join(music_dir , songs[-1]))
 
        elif 'time' in query:
            strTime =datetime.datetime.now().strftime("%H;%M;%S")
            speak(f"Sir! the time is {strTime}")
        
		
        elif 'how are you' in query:
            speak("I am absolutely fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me JARVIS")   
 
        elif 'exit' in query:
            speak("Thank you!!")
            exit()
 
        elif "who made you" in query or "who created you" in query: 
            speak("There are three persons who made me. Mohit , Tejasvi and, Tanmay")

        elif "invigilating" in query: 
            speak("Profesor Rohan sir , Profesor Swati mam")
            
           

        elif "code" in query:
            codepath = r"C:\\Users\\MOHIT VILAS GIRI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(codepath)

        elif "firefox" in query:
            chromepath = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            os.startfile(chromepath)

        elif "chrome" in query:
            chromepath = r'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome'
            os.startfile(chromepath)

        elif "note" in query:
            chromepath = r'C:\\Users\\MOHIT VILAS GIRI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
            os.startfile(chromepath)


        elif "open board" in query:
            openpath = r'C:\\Users\\MOHIT VILAS GIRI\\Desktop\\new\\TP\\new 1\\TASK EYRC 2020\\ML AND GRP 7 TASK\\arduino-1.8.9\\arduino.exe'
            os.startfile(openpath)


        elif 'on the led' in query:
            speak('ok!!')
            board.digital[10].write(1)


        elif 'off the led' in query:
            speak('ok!!')
            board.digital[10].write(0)

        elif 'on the led1' in query:
            speak('ok!!')
            board.digital[11].write(1)


        elif 'off the led1' in query:
            speak('ok!!')
            board.digital[11].write(0)
