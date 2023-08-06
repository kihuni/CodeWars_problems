def rot13_decrypt(text):
    # initializing an empty string result for storing decrypted characters
    result = ''
    # this begins the for loop
    for char in text:
        # this check if the current `char` is an uppercase letter
        # range from (A-Z). if its uppercase the following code is
        # excecuted
        if 'A' <= char <= 'Z':
            # Here we are performing the ROT13 decryption for an  uppercase letter
            # ord(char) gives ascii value for the character and ord('A') gives
            # the ascii value of 'A'. The difference between these gives us the
            # position of the character in alphabet(0 for A, 1 for B, etc)
            # Then we add 13 to this position (ROT13 shift) and find the remainder 
            # divide by 26; this makes sure that the result is wraps around back to the
            # start of the alphabet if it goes beyond 'Z'
            # We then add 'ord('A') back to shift the result back into the ascii range
            # of the uppercase letters. 'chr() converts this ascii value into a 
            # character, we then add this characters to result
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            # this checks if the current characters is a lowercase letter. 
            # if character is lowercase letter, the following code is executed
        elif 'a' <= char <= 'z':
            # this does the same thing as upper code but for lowercase letters
            result += chr((ord(char) - ord('a')+ 13) % 26 + ord('a'))
            # This checks if the character is neither an uppercase nor a 
            # lowercase letter (such as a punctuation symbol or space).
        else:
            result += char
     # if reult is no a charater return result without changes   
    return result
print(rot13_decrypt('EBG13 rknzcyr'))
        
            
            
            