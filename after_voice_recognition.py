import voice_analyser
import pyttsx3
import speech_recognition as sr
import datetime


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


if __name__ == "__main__":
    voice_analyser.speak("Speak the command now")
    # Get the text from the audio input
    query = voice_analyser.voice_recognition()
    # Return the text
    print(query)

    # If the user enters 2, then the user wants to use text command
    if query == "hello":
        print("confirmed")
    elif query == "record":
        recordAudio()
    elif query == "time":
        speakTime()
    elif query == "date":
        speakDate()
    else:
        print("Invalid choice. Please try again")
