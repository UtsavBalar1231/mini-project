from datetime import datetime

def date_time():
    now = datetime.now()
    print("Current date and time:")
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    
if __name__ == "__main__":
    date_time()
    