def square_concatenate(num):
    # change the input into string
    str_num = str(num)

    # Initialize an empty string to hold the concatenated squares

    concatenated = ""

    # iterate over each digit in the string and square it

    for digit in str_num:
        square_digits = str(int(digit)**2)
        concatenated+=square_digits

    # Convert the concatenated squares back to an integer

    concatenated_int = int(concatenated)


    return concatenated_int


print(square_concatenate(9119)) # Output: 811181
print(square_concatenate(765))  # Output: 493625