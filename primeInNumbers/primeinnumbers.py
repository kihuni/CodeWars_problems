def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factor_decomposition(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append((i, count))
            i += 1

    if n > 1:
        factors.append((n, 1))

    decomposition = ""
    for factor, count in factors:
        if count == 1:
            decomposition += f"({factor})"
        else:
            decomposition += f"({factor}**{count})"

    return decomposition


n = 86240
result = prime_factor_decomposition(n)
print(result) #(2**5)(5)(7**2)(11)
