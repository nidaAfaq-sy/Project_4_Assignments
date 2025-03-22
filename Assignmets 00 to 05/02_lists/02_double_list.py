def main():
    nums = [1, 2, 3, 4]  # Renamed 'numbers' to 'nums' for brevity

    for index in range(len(nums)):  # More descriptive loop variable
        nums[index] *= 2  # Simplified in-place multiplication

    print(nums)  # Prints the updated list


if __name__ == '__main__':
    main()
