import speech_recognition as sr
import webbrowser
import pyttsx3
#import requests

# here we use the and install the pocketsphinx

recognizer =sr.Recognizer()
engine =pyttsx3.init()

#API key for the news
newsapi = "b3c86d51678f4a3ea40ec1be8aafd921"

def speak(text):
    # convert the text inot speech
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    comand=command.lower()
    print(f"Command received: {command}")  # Debuggingz
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")        
    elif "news" in command:
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # prase the json response
            data = r.json()
            # extract the articles
            articles = data.get('articles',[])
            # print the head lien
            for article in articles:
                speak(article.get['title'])
            
if __name__ ==  '__main__':
    speak("initializing shivam......")
    while True:
        # listen the wake word shivam
        # obtain audio from the microphone
        recognizer = sr.Recognizer()
        

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise effect
                print("Listening....")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
            command = recognizer.recognize_google(audio)
            if(command.lower() == "shivam"):
                speak("Yaa")
                # listen for command
                with sr.Microphone() as source:
                    print("shivam Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)                                                                            

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))