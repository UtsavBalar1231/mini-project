import pyttsx3
import speech_recognition as sr
import datetime
import voice_analyser
import wikipedia
import webbrowser

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    while True:
        try:
            # Uses the default API
            data = r.recognize_google(audio)
            print("You said: " + data)

            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.save_to_file(data, 'output.mp3')
            engine.runAndWait()

            break

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))


def speakTime():
    time = datetime.datetime.now()
    voice_analyser.speak("The time is " + str(time.hour %
                                              12) + " " + str(time.minute) + "O'clock")


def speakDate():
    date = datetime.datetime.now()
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    voice_analyser.speak("The date is " + str(date.day) +
                         " " + months[date.month - 1] + " " + str(date.year))
    
def WikipediaSearch():
    voice_analyser.speak("What do you want to search on Wikipedia?")
    query = voice_analyser.voice_recognition()
    results = wikipedia.summary(query, sentences=2)
    voice_analyser.speak("According to Wikipedia")
    voice_analyser.speak(results)
    
def BrowserSearch():
    voice_analyser.speak("What do you want to search on the browser?")
    query = voice_analyser.voice_recognition()
    webbrowser.open_new_tab(query)
    voice_analyser.speak("Here is what I found for " + query)
