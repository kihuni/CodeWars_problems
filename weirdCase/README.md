You are required to write a function toWeirdCasethat accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zeroith index is even, therefore that character should be upper cased and you need to start over each word.

The passed in string will only consist of alphabetical characters and spaces(''). spaces will only be present if there are multiple words. Words will be separated by single space('')

# Solution
The function splits the string into words`["hello", "world"]`and then processes each word individually.
it converts the character to lowercase using `char.lower()`. The modified characters are then joined back together to form the weird-cased word. Finally, the function joins the weird-cased words with spaces using `" ".join(result)` and returns the resulting string. [solution](https://github.com/kihuni/CodeWars_problems/blob/main/weirdCase/weirdcase.py)
