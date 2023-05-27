def to_camel_case(text):
    if not text:
        return text
    
    words = text.replace('-', '_').split('_')
    print(words) # ['the', 'stealth', 'warrior']
    return words[0] + ''.join(word.capitalize() for word in words[1:])

input_text = "the-stealth-warrior"

to_camel_case_text = to_camel_case(input_text)
print(to_camel_case_text) # theStealthWarrior