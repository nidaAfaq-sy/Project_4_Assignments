MINIMUM_HEIGHT: float = 50.0  # Arbitrary units :)

def main():
    try:
        height = float(input("How tall are you? ").strip())
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride! 🎢")
        else:
            print("You're not tall enough to ride, but maybe next year! 😊")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
