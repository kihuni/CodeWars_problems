A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

## Solution
The function first creates a set called alphabet which contains all lowercase letters of the English alphabet using the string.ascii_lowercase constant.

It then converts the input sentence to lowercase using the lower() method and creates a set called letters containing all the unique lowercase letters present in the sentence.

Finally, it checks if the alphabet set is a subset of the letters set using the issubset() method. If all the letters of the alphabet are present in the sentence, it returns True; otherwise, it returns False.
[code]()