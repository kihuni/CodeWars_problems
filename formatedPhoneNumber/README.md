You are required to write a function that accept an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

## Example
`create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"`

## Solution
`create_phone_number` fuction takes an array of `n` as input, then checks if the length of the `n` if its not equal to 10. if its not it returns an error.

Then, it formats the phone number by joining the elements of the array in the appropriate places. The resulting formatted phone number is then returned. [code]()