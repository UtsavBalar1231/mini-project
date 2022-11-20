import os
import voice_analyser

# Keywords to authenticate the user
keywords = ["hey", "hello", "hey ace", "hi ace", "hello ace"]

def authenticate_text(key):
    """
    This function authenticates the user using text command
    """
    
    # If the user enters the correct password, then the user is authenticated
    if key in keywords:
        print("Welcome to ACE!")
        # Run the after_text_recognition.py file
        os.system("python3 after_text_recognition.py")
        return True
    else:
        print("Invalid command. Please try again")
        return False
    
def authenticate_voice(key):
    """
    This function authenticates the user using voice command
    """
    if key in keywords:
        print("Welcome to ACE!")
        voice_analyser.speak("Authenticated, Welcome to ACE!")
        
        # Run the after_voice_recognition.py file
        os.system("python3 after_voice_recognition.py")
        return True
