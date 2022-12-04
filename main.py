import authenticator
import voice_analyser
import os


def start():
    print("Welcome to ACE!")
    print("Enter your choice:")
    print("1. for voice command")
    print("2. for text command")

    # Get the choice from the user
    choice = input()
    if choice == "1":
        # Run the after_voice_recognition.py file
        os.system("python3 after_voice_recognition.py")
    # If the user enters 2, then the user wants to use text command
    elif choice == "2":
        print("Using text command")
        while True:
            key = input("Enter the password: ")
            if authenticator.authenticate_text(key):
                break
            else:
                print("Invalid command. Please try again")
    else:
        print("Invalid choice. Please try again")


if __name__ == "__main__":
    loop = True
    while loop:
        try:
            query = voice_analyser.voice_recognition()
            if query == 0:
                print("Sorry, I didn't get that")
                continue
            elif authenticator.authenticate_voice(query):
                loop = False
                start()
            else:
                continue
        except KeyboardInterrupt:
            print("Goodbye")
            break
