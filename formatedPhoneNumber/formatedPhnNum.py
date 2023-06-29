def create_phone_number(n):
    if len(n) != 10:
        return "Invalid input: array must contain exactly 10 integers"
    
    formatted_num = "(" + "".join(map(str, numbers[:3])) + ") " + "".join(map(str, numbers[3:6])) + "-" + "".join(map(str, numbers[6:]))
    return formatted_num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
phone_number = create_phone_number(numbers)
print(phone_number) #(123) 456-7890"