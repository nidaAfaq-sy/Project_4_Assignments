def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks to create a fun story.\n")

    # Asking for user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Predefined Mad Libs story template
    story = f"""
    One day, a {adjective} {noun} decided to {verb} at the {place}.
    Everyone was surprised and started laughing.
    It was the most unexpected thing that had ever happened there!
    """

    # Print the completed Mad Libs story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Run the Mad Libs game
if __name__ == "__main__":
    mad_libs()
