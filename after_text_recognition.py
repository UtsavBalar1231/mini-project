if __name__ == "__main__":
    while True:
        print("Enter your choice:")
        print("1. for calculator")
        print("2. for date and time")
        print("3. for text editor")
        print("4. for voice recorder")
        
        choice = input()
        
        if choice == "1":
            print("calculator")
            break
        elif choice == "2":
            print("date and time")
            break
        elif choice == "3":
            print("text editor")
            break
        elif choice == "4":
            print("voice recorder")
            break
        else:
            print("Invalid choice. Please try again")
    
    