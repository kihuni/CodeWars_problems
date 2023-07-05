Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

```
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

```
[Here](https://github.com/kihuni/CodeWars_problems/blob/main/HumanReadableTime/humanreadabletime.py) we are defining a function named format_time that takes a single parameter seconds. The if statement checks if the input seconds is less than 0 or greater than 359999. If either of these conditions is true, it means the input is invalid. In such cases, a ValueError is raised with an appropriate error message.

Next, first, we are converting `seconds` into whole `hour` performing integer division. Since there are `3600 seconds` in an hour, the result will be the number of hours.

second, We are calculating the number of minutes remaining after accounting for the hours. The modulo operator `%` is used to get the remaining seconds after subtracting the `hours (seconds % 3600)`. Then, integer division is performed by 60 to get the number of minutes.

finally, We calculates the number of `seconds` remaining after accounting for the `hours and minutes`. The modulo operator` % `is used to get the remaining seconds after subtracting the hours and minutes.
