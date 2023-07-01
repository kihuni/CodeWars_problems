def digital_root(n):
    while n >= 10:
        digit_sum = sum(int(digit) for digit in str(n))
        
        # We update the value of n to be digit_sum
        n = digit_sum
    return n


print(digital_root(132189)) #6