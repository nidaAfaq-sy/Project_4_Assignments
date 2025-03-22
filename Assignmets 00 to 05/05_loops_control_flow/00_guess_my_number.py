import random

def guess_my_number():
    number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
                continue
            
            if guess > number:
                print("Your guess is too high")
            elif guess < number:
                print("Your guess is too low")
            else:
                print(f"Congrats! The number was: {number}")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    guess_my_number()
