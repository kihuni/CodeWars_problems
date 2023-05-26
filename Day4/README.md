There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

### solution 

To solve this, first, you iterate though the list of integer pairs and keep track of number of people on the bus. Then substract the number of people getting off and add the number of people getting on at each bus stop.

Finally, return the total number of people remaining on the bus. 



### Code Explanation
In this example, the `number` function takes a list if integer pairs `bus_stops` as input. Then it initializes the `totalpassagers` variable to keep track of the number of people on the bus.

It then iterates through each `stop` in the `bus_stops` list. For each stop, it extracts the number of people getting on and getting off the bus. Next subtracts the number getting off and adds the number if people getting on the`totalpassagers` count

Finally, the function returns the `totalpassagers` count, ensuring it is non-negative using th `max` function to handle cases where the bus ends up empty.[solution]()
