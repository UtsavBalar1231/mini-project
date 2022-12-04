import voice_analyser
import voiceFunctions

if __name__ == "__main__":
    voice_analyser.speak("Speak the command now")
    # Get the text from the audio input
    query = voice_analyser.voice_recognition()
    # Return the text
    print(query)

    if query == 0:
        voice_analyser.speak("Sorry, I didn't get that")

    if "time" in query:
        voiceFunctions.speakTime()

    elif "date" in query:
        voiceFunctions.speakDate()

    elif "record" in query:
        voiceFunctions.recordAudio()

    elif "wikipedia" in query:
        voiceFunctions.WikipediaSearch()

    elif "browser" or "browse" or "websearch" or "search" in query:
        voiceFunctions.BrowserSearch()

    elif "exit" or "close" in query:
        voice_analyser.speak("Goodbye")
        exit()
        
    else:
        voice_analyser.speak("Sorry, I didn't get that")
