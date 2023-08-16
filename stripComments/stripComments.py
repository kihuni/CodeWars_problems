def solution(string, markers):
    # split the string into lines
    lines = string.split('\n')
    print(lines)
    
    # process each line
    for line in range(len(lines)):
        for marker in markers:
            # if a marker us found, cut the string up to that marker
            if marker in lines[line]:
                lines[line] = lines[line].split(marker)[0]
        # remove any trailling whitespace from the line
        lines[line] = lines[line].rstrip()
        
    
    # joine the processed lines back into a single string
    return '\n'.join(lines)

# Test the function
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(result)  # Expected output: "apples, pears\ngrapes\nbananas"







            
            