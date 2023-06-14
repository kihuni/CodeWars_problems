You are required to find the maximum sum of a contiguous subsequence in an array or list of integers.
In that when the list is made up of negatives number, return 0 

## Example:
```
sequence([-2, 1, -3, 4, -1, 2, 1,-5, 4]) # 6

```
# Explanation

We initialize two variables: `max_sum` and `current_sum` to 0. These variables will keep track of the maximum sum found so far and the sum of the current subarray, respectively.
We start iterating through the input list.for each number `num` in the list, we perform the following steps:
    We update the `current_sum` by adding the current number `num` to it. Howeever, if the `current_sum` becomes negative,we reset it to 0. We take the maximum between 0 and `current_sum + num` to reset `current_sum`

We update the `max_num` by taking the maximum between the current`max_num` and the updated`current_num`. This allows to keep track of the maximum sum found so far
    
After iterating the entire list we return `max_num`as the result

# This is how it works
```
Iteration 1: num = -2
current_sum = max(0, 0 + (-2)) = 0
max_sum = max(0, 0) = 0
Iteration 2: num = 1
current_sum = max(0, 0 + 1) = 1
max_sum = max(0, 1) = 1
Iteration 3: num = -3
current_sum = max(0, 1 + (-3)) = 0
max_sum = max(1, 0) = 1
Iteration 4: num = 4
current_sum = max(0, 0 + 4) = 4
max_sum = max(1, 4) = 4
Iteration 5: num = -1
current_sum = max(0, 4 + (-1)) = 3
max_sum = max(4, 3) = 4
Iteration 6: num = 2
current_sum = max(0, 3 + 2) = 5
max_sum = max(4, 5) = 5
Iteration 7: num = 1
current_sum = max(0, 5 + 1) = 6
max_sum = max(5, 6) = 6
Iteration 8: num = -5
current_sum = max(0, 6 + (-5)) = 1
max_sum = max(6, 1) = 6
Iteration 9: num = 4
current_sum = max(0, 1 + 4) = 5
max_sum = max(6, 5) = 6
After iterating through the entire list, we return max_sum, which is 6. Therefore, the maximum sum subarray in the given list is
```
[code](https://github.com/kihuni/CodeWars_problems/blob/main/max_sum_subarray/max_sum_array.py)
