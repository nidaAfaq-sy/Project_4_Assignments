import time

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"\rTimer: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        total_seconds -= 1
    
    print("\nTime's up! 🎉")

if __name__ == "__main__":
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        if minutes < 0 or seconds < 0 or seconds >= 60:
            print("Please enter valid minutes and seconds.")
        else:
            countdown_timer(minutes, seconds)
    except ValueError:
        print("Invalid input! Please enter numeric values.")
