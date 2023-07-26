def pig_it(text):
    words = text.split() # split the input text
    res = [] # initialize an empty list to store word after it has been converted to pig latin
    for word in words:
        if word.isalpha(): # checks if words is all letters no punctuation
            res.append(word[1:] + word[0] + 'ay') # moves the first letter to the end and adds ay
        else:
            res.append(word) #This will leave punctuation marks untouched
    return ''.join(res)

print(pig_it('Pig latin is cool'))   