Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
`result should == "apples, pears\ngrapes\nbananas"`

## Solution
To achieve this solution, you can split the input string by lines, and for each line, check for the existence of any of the comment markers. Once you encounter a comment marker, you can strip the remainder of the line. [Here's how you can implement this:](https://github.com/kihuni/CodeWars_problems/blob/main/stripComments/stripComments.py)
