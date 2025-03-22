def calculate_sum(numbers: list[int]) -> int:
    """
    Given a list of integers, returns their total sum.
    """
    return sum(numbers)  # Using built-in sum function


def main():
    num_list: list[int] = [1, 2, 3, 4, 5]  # Define a list of numbers
    total: int = calculate_sum(num_list)  # Compute the sum
    print(f"The sum is: {total}")  # Display the result


if __name__ == "__main__":
    main()
