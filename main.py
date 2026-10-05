import speech_recognition as sr
import webbrowser
# import pyttsx3
import musicLibrary
import pywhatkit
import requests
import pygame
import os

from openai import OpenAI
from gtts import gTTS
from dotenv import load_dotenv


# Load API keys from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

newsapi = os.getenv("NEWS_API_KEY")




#Speak function 
#gTTS -> MP3 ->pygame -> Speaker
def speak(text):

    print("Jarvis:", text)

    try:

        # Text -> MP3
        tts = gTTS(
            text=text,
            lang="en",
            timeout=5
        )

        tts.save("jarvis.mp3")

        # MP3 -> Speaker
        pygame.mixer.init()

        pygame.mixer.music.load("jarvis.mp3")
        pygame.mixer.music.play()

        # Wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pass

        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception as e:

        print("TTS Error:", type(e).__name__, e)

#openAI 


def ai_response(question):

    try:

        print("Sending question to OpenAI:",question)

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=(
                 "You are Jarvis, a helpful voice assistant. "
                "Answer the user in simple English. "
                "Keep the answer short and easy to understand "
                "because your answer will be spoken aloud.\n\n"
                f"User: {question}"
            )
        )

        answer = response.output_text
        if answer:
            print("AI Answer:", answer)
            speak(answer)
        else:
            speak("Sorry, I could not generate a response.")

    except Exception as e:

        print("OpenAI Error:", type(e).__name__, e)

        speak(
            "Sorry, I am having trouble connecting "
            "to the AI service."
        )

#Command Processing
def processCommand(c):

    c = c.lower().strip()
    print("Processing command:", c)

    #open websites based on user command

    if "google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    
     #play music based on user command

    elif c.startswith("play"):

     #"play bihari"-> "bihari"
        song = c.replace("play", "", 1).strip()

        print("Searching for song:", song)

        if song in musicLibrary.music:

            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak("Playing"+song)

        else:

            speak("Playing "+song)
        #song search on YouTube
            pywhatkit.playonyt(song)

    #fetching news 
    elif "news" in c.lower():

        url = (
            f"https://newsapi.org/v2/top-headlines?"
            f"category=technology&language=en&apiKey={newsapi}"
        )

        try:

            r = requests.get(url)

            print("Status Code:", r.status_code)

            if r.status_code == 200:

                data = r.json()
                articles = data.get("articles", [])

                if articles:

                    speak("Here are the latest technology news.")

                    for article in articles[:5]:

                        title = article.get("title")

                        if title:
                            print(title)
                            speak(title)

                else:

                    print("No articles found.")
                    speak("Sorry, no news headlines available.")

            else:

                print("News API Error:", r.text)
                speak("Sorry, I could not fetch the news.")

        except Exception as e:
            print("News Error:",type(e).__name__,e)
            speak("Sorry, I could not connect to the news service.")

    


    #stop or exit command handling
    elif c in ["stop", "exit", "quit" , "bye","bye-bye",
               "goodbye", "see you later", "see you soon",
                 "see you", "ok bye", "ok bye-bye",
                   "ok goodbye","bye jarvis","bye-bye jarvis",
                   "ok bye jarvis","jarvis bye","jarvis bye-bye",
                   "jarvis goodbye",]:

        speak("Goodbye! Have a great day.")
        return False

#openAI Fallback
    else:
        print("Command not recognized.")
        print("Sending command to OpenAI:", c)

        ai_response(c)        
    return True

    

#main function to initialize Jarvis and listen for commands


if __name__ == "__main__":

    #create a speech recognizer instance
    r = sr.Recognizer()
    r.operation_timeout = 5

    #microphone calibration for ambient noise
    with sr.Microphone() as source:

        print("Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)

    print("Microphone Ready to listen.")
    #start jarvis
    speak("Initializing Jarvis")

    #Main loop
    while True:

        try:

#wake word detection and listening for commands

            with sr.Microphone() as source:

                print("Listening...")

                audio = r.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = r.recognize_google(audio)

            print("You said:", word)

#jarvis activation and command processing

            if word.lower() == "jarvis":

                speak("Yaa")
                #jasvis is active
                with sr.Microphone() as source:

                    print("Jarvis Active...")

                    audio = r.listen(source,
                                     timeout=5,
                                     phrase_time_limit=5
                                     )

                    command = r.recognize_google(audio)

                    print("You said:", command)

                    #process command
                    if not processCommand(command):
                        break

                    print("command processed successfully.")

        #no speech detected within the timeout period
        except sr.WaitTimeoutError:

            continue

        #voice not recognized or speech recognition errors handling
        except sr.UnknownValueError:

            continue

        #Internet / Google speech recognition service errors handling
        except sr.RequestError as e:

            print("Speech recognition error:", e)
            continue

        #stop jarvis on keyboard interrupt
        #use also Ctrl+C to stop the program
        except KeyboardInterrupt:

            print(" Jarvis stopped.")
            break

        #other exceptions handling
        except Exception as e:

            print("Error:", type(e).__name__, e)
