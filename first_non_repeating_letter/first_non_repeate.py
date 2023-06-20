def first_non_repeating_letter(s):
    # Convert the string to lowercase for case-insensitive comparisons
    s = s.lower()
    
    # Counts the occurences of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0)+1
        
    
    for char in s:
        if char_counts[char] == 1:
            return char if char in s else char.upper()
        
    
    return ""
print(first_non_repeating_letter('stress'))
        