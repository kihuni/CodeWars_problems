 You are asked to create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

 ### Example usage

```
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

```

### solutions
I this example we are using list comprehension to create a new list by iterating over the list and applying the condition `isinstance()` function to filter out any string in the lists. [solution](https://github.com/kihuni/CodeWars_problems/blob/main/Day2/day2.problem.py)
