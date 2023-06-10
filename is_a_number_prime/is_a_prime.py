import math

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 ==0:
        return False
    
    sqrt_n = math.isqrt(num)
    divisor = 5
    while divisor <= sqrt_n:
        if num % divisor == 0 or num % (divisor + 2) == 0:
            return False
        divisor += 6
        
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))