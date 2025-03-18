import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import requests
import musicList


# initializing Parameter
engine=pyttsx3.init()
speaking=True
newsapikey="c28294f5f5d44ccfb2aa4200aa373e23"


# Function to convert text to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)  # Allow time for audio playback before script exits


# Actions which can Rocket Perform

def doAction(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")

    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")

    elif "open spotify" in command.lower():
        webbrowser.open("https://spotify.com")

    elif command.lower().startswith("play"):
        musicname=command.lower().split(" ")[1]
        webbrowser.open(musicList.musicNames[musicname])

    elif "news" in command.lower():
        print("News comming")
        datarequest=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}")
        if datarequest.status_code == 200:
            # parse the json request
            data=datarequest.json()

            # extract the articles
            articles=data.get('articles',[])

            #speak the HeadLines
            for article in articles:
                speak(article['title'])

    else:
        print("nothing")



    





if __name__ == "__main__":
    speak("Initializing Rocket")



    while speaking:
        # listen for the word popla
        # obtain audio from microphone

        

        try:
            r=sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)


            print("Recognizing...")
            command =r.recognize_google(audio)  

            if(command.lower()=="exit"):
                print("Exiting")
                speaking=False
            
            elif(command.lower()=="rocket"):
                speak("Yes Nishit")

                newcommand=True
        
                print("Rocket is Activated!")
                
                while(newcommand):
                    try:
                        with sr.Microphone() as source:
                            print("Listening Nishit....")
                            audio=r.listen(source)
                            command=r.recognize_google(audio)
                            print(command)
                            if(command.lower() != "exit"):
                                doAction(command)
                            else:
                                newcommand=False
                                print("Exiting")
                    except Exception as e:
                        print("Error; {0}".format(e))
                            

            else:
                print(command)  



        except Exception as e:
            print("Error; {0}".format(e))
        


