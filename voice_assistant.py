import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


      
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
        print(e)    
        print("Unable to Recognizing your voice.")  
        return "None"
    return query
  
     


if _name_ == '_main_':
    speak("Amigo assistance activated")
    speak("How can i Help you, Mam")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Answer From Wikipedia")
            print(results)
            speak(results)

        elif "are you" in query:
            speak("I am amigo developed by Saiteja")

        elif "wikipedia" in query and "hindi" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("hindi", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            r = sr.Recognizer()
            results = r.recognize_google(results, language='hi')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Taking You To Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Taking you to Google\n")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")
       
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")     

        elif "send a whatsaap message" in query or "send a WhatsApp message" in query:
            driver = webdriver.Chrome('Web Driver Location')
            driver.get('https://web.whatsapp.com/')
            speak("Scan QR code before proceding")
            webbrowser.open("whatsapp.com")   

        elif 'play music' in query or "play song" in query or "gaana"in query or "song" in query:
            #music_dir = "G:\\Song"
            username = getpass.getuser()
            music_dir = "C:\\Users\\"+username+"\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            random=os.startfile(os.path.join(music_dir, songs[1]))

        elif 'local disk d' in query:    
            speak("opening local disk D")
            webbrowser.open("D://")

        elif 'local disk c' in query:    
            speak("opening local disk C")
            webbrowser.open("C://")

        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Saiteja.")
