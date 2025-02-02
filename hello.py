from datetime import datetime

def get_time_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def greet(name=None):
    time_greeting = get_time_greeting()
    if name:
        print(f"{time_greeting}, {name}!")
    else:
        print(f"{time_greeting}, World!")

def main():
    greet()

if __name__ == "__main__":
    main()
