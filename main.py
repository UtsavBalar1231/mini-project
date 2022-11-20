import authenticator
import voice_analyser

if __name__ == "__main__":
    loop = True

    while loop:
        print("Welcome to ACE!")
        print("Enter your choice:")
        print("1. for voice command")
        print("2. for text command")

        # Get the choice from the user
        choice = input()
        if choice == "1":
            # print("voice command")
            
            # Loop until the user enters a valid command
            while True:
                # Try to authenticate the voice command
                try:
                    key = voice_analyser.analyse_voice()
                    print("key: ", key)
                    
                    # If the command is valid, break the loop
                    if authenticator.authenticate_voice(key):
                        loop = False
                        break
                    else:
                        print("Invalid command. Please try again")
                # Exception handling to handle exceptions at the runtime
                except Exception as e:
                    print("Error playing audio file: ", e)
                    print("Please try again")
                    
        # If the user enters 2, then the user wants to use text command
        elif choice == "2":
            print("Using text commands")
            while True:
                key = input("Enter the password: ")
                if authenticator.authenticate_text(key):
                    loop = False
                    break
                else:
                    print("Invalid command. Please try again")
        else:
            print("Invalid choice. Please try again")
