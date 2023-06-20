You are required to write a function named first_non_repeating that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests. using python

# Solution

- First, the function converts the input string `s` to lowercase using the `lower()` method.This is done to make the comparison case-insensitive.
- Second, it initialize an empty dictionary `char_counts` to store the count of each character in the string.
The `for` loop iterates over each character `char` in the string `s`. From `char_counts` 'defaulting to 0 if character is not yet present', increments the count by 1, and assigns the update count back to `char_counts[char]`. This way, `char_counts` keeps track of the number of occurrences of each character in the string
- Third, It iterates over each character `char` in the string `s` again, it checks if the count of the character `char` in `char_counts` is equal to 1. if so, it returns the character `char`.
However, to maintain the original case of the character,it first checks if `char` is present in the original string `s`. if it is, it returns `char` as it is. Otherwise, it returns the uppercase version of `char` using the `upper()` method
- Finally,If no non-repeating character is found in the string, the function returns an empty string "". [solution]()