According to [Wikipedia](https://en.wikipedia.org/wiki/Digital_root):

The `digital root` (also repeated digital sum) of a natural number in a given radix is the (single digit) value obtained by an iterative process of summing digits, on each iteration using the result from the previous iteration to compute a digit sum. The process continues until a single-digit number is reached. For example, in base 10, the digital root of the number `12345` is`6` because the sum of the digits in the number is `1 + 2 + 3 + 4 + 5 = 15`, then the addition process is repeated again for the resulting number 15, so that the sum of `1 + 5 equals 6`, which is the digital root of that number.

Given n, You are required to take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

# Examples
```
16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

```
