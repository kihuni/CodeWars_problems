import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    print(alphabet)
    letters = set(sentence.lower())
    print(letters)
    return alphabet.issubset(letters)
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence)) 