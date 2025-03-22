MAX_VALUE = 10000  # Define the maximum value for Fibonacci terms

def fibonacci_sequence(max_value):
    a, b = 0, 1
    while a < max_value:
        print(a, end=" ")
        a, b = b, a + b

# Call the function to generate the sequence
fibonacci_sequence(MAX_VALUE)
