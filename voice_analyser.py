import pyttsx3
import speech_recognition as sr
import time

def voice_recognition():
    """
    This function converts the audio input to text using Google Speech Recognition
    """
    # Initialize the recognizer
    r = sr.Recognizer()

    while True:
        # Exception handling to handle exceptions at the runtime
        try:
            # Use the microphone as source for input.
            with sr.Microphone() as source:
                # Wait for half a second to let the recognizer adjust the
                # r.adjust_for_ambient_noise(source, duration=0.2)

                # Listen to the audio input
                print("Listening...")
                speak("Listening")
                audio = r.listen(source)
                # time.sleep(1)
                
                # Recognize speech using Google Speech Recognition
                print("Recognizing...")
                speak("Recognizing")
                # Convert the audio input to text
                query = r.recognize_google(audio)
                print("You said: " + query)
                # Return the text
                return query.lower()
        except sr.UnknownValueError:
            print("Ace Could not understand audio")
        except sr.RequestError as e:
            print("Ace Could not request results {0}.".format(e))


def speak(input):
    """
    This function converts the text to speech using Python Text-to-Speech API
    and plays the audio file
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(input)
    engine.runAndWait()
    time.sleep(1)


def analyse_voice():
    """
    This function analyses the voice input and returns the key
    """
    speak("Hello, I am ACE. You are using voice control.")
    # Get the text from the audio input
    query = voice_recognition()
    print(query)
    # Return the text
    return query
