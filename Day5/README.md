You are required to complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

### Examples 

```
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

```

# Solution Explained

The `to_camel_case` function takes a string `text` as input and returns the camel case version of the string.

It first replace any dashes with undescores to ensure consistent splitting of words. it then splits the text into words using underscores the delimiter.
The first word is added as is, while the subsequent words are capitalized.Finally, the words are joined together to form the camel case string. [solution](https://github.com/kihuni/CodeWars_problems/blob/main/Day5/day5.problem.py)


