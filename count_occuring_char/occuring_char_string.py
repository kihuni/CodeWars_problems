def count(s):
    # Create an empty dictionary to store the characters counts
    char_counts = {}
    
    # iterates over each characters in the string
    for char in s:
        # increment the count for the character if it already exists in the
        # or initialize it to 1 if its a new character
        char_counts[char] = char_counts.get(char, 0) + 1
        
    return char_counts



print(count('aba')) #{'a': 2, 'b': 1}