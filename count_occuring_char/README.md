You are required to define a function that counts all the characters in a given string. For example, a string like `aba` result should be `{'a':2, 'b':1}`. result for an empty string should be an empty object literal `{}`

# solution

The `count` function takes a string as input and initilizes an empty dictionary `char_counts` to store the characters counts.it then iterates over each character in the string and updates the count accordingly.

The `get` method is used to handle the case when a character is encountered for the first time and is not yet present in the dictionary. FInaly the function returns the `char_counts` dictionary
[solution](https://github.com/kihuni/CodeWars_problems/blob/main/count_occuring_char/occuring_char_string.py)
