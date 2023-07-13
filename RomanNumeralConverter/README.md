Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals `1990` is rendered: `1000=M, 900=CM, 90=XC;` resulting in `MCMXC`. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI

`input range : 1 <= n < 4000`

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

## Solutions Explained

On the first function, it takes an integer `n` as input and initializes a dictionary `roman_numerals` that maps integer values to their corresponding roman numerals symbols.

Next, the function initializes an empty string `roman`.it then iterates over the `roman_numerals`dictionary, which contains the roman numerals in descending order of their values.

In the loop, it checks if the current number`num` is less than or equal to the given integer`n`. if so, it appends the corresponding symbol to the `roman` string and subtracts the number from `n`. This is done to keep track of the remaining numbers of `n`.

Finally, it returns `roman` string representing the given integer in roman numerals

On the second function, the function takes a string `roman`as input and initializes a dictionary `roman_numerals` that maps roman numerals symbols to their corresponding integers values.

Next, it initializes the variable `number` to 0 and sets `i` to 0 as the index to iterates over the `roman` string.

Inside the loop, it checks if the current two characters in the roman string (starting from index i) form a valid Roman numeral symbol. If so, it adds the corresponding value to number and increments i by 2 to skip those two characters. Otherwise, it adds the value of the current character to number and increments i by 1.

This process continues until all characters in the roman string are processed. Finally, it returns the resulting number as the integer value corresponding to the given Roman numeral.
