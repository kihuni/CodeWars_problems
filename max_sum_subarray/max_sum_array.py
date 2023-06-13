def max_sequence(arr):
    if not arr:
        return 0
    
    # Initialize max_sum and current to hold the
    # updated sum and the current sum
    max_sum = 0
    current_sum = 0
    
    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1,-5, 4]))