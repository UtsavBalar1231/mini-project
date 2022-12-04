import os

if __name__ == "__main__":
    while True:
        print("Enter your choice:")
        print("1. for calculator")
        print("2. for date and time")
        print("3. for text editor")
        print("4. for voice recorder")
        print("5. for voice to text")
        print("6. for settings alarm")

        choice = input()

        if choice == "1":
            os.system("python ./textFunctions/calculator.py")
            break
        elif choice == "2":
            os.system("python ./textFunctions/date_time.py")
            break
        elif choice == "3":
            os.system("python ./textFunctions/text_editor.py")
            break
        elif choice == "4":
            os.system("python ./textFunctions/voice_recorder.py")
            break
        elif choice == "5":
            os.system("python ./textFunctions/voice_to_text.py")
            break
        elif choice == "6":
            os.system("python ./textFunctions/set_alarm.py")
            break
        else:
            print("Invalid choice. Please try again")
