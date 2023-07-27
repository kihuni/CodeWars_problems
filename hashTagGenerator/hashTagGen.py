def generate_hastag(s):
    # check if the input is empty
    if not s:
        return False
    
    # Remove leading and trailing whitespace, split the string into words
    words = s.strip().split()
    
    # capitalize the first letter of each word
    words = [word.capitalize() for word in words]
    print(words)
    
    # join the words together with no space, add a hashtag at the beggining
    
    hashtag = '#' + ''.join(words)
    
    # if the hashtag value is too long, return false
    if len(hashtag) > 140:
        return False
    
    return hashtag

print(generate_hastag("    Hello     World   ")) # #HelloWorld