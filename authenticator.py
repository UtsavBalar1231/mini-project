import os
import voice_analyser

def authenticate_text(key):
    """
    This function authenticates the user using text command
    """
    passwords = ["hello ace", "hey ace", "hi ace"]
    # If the user enters the correct password, then the user is authenticated
    if key in passwords:
        print("Welcome to ACE!")
        print("Authenticated, Welcome to ACE!")
        
        # Run the after_text_recognition.py file
        os.system("python3 after_text_recognition.py")
        return True
    else:
        print("Invalid command. Please try again")
        return False
    
def authenticate_voice(key):
    voice_keywords = ["hey", "hello", "hi"]

    """
    This function authenticates the user using voice command
    """
    for k in key.split():
        if k in voice_keywords:
            print("Welcome to ACE!")
            voice_analyser.speak("Authenticated, Welcome to ACE!")
            return True
        
