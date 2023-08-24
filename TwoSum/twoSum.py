def twoSum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_dict = {}
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        # If the complement exists in the dictionary, we've found our pair
        if complement in num_dict:
            return [num_dict[complement], i]
        # Otherwise, store the current number and its index in the dictionary
        num_dict[num] = i
        
print(twoSum([2,7,11,15], 9))  # Expected output: [0,1]
print(twoSum([3,2,4], 6))      # Expected output: [1,2]
print(twoSum([3,3], 6))        # Expected output: [0,1]