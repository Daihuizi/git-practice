def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    # Test comment
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
#newest comment
    return max_num

#this function helps in finding max_value
if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))