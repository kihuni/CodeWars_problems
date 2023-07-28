def cakes(recipe, available):
    num_cakes = [] # initilizes an empty list
    
    # the for loop iterates over each ingridients
    # and its amount in the recipe
    # and returns a list of tuples where
    # each tuple contains a key-value pair
    # from the dictionay
    for ingredients, amount in recipe.items():
        # This checks if the current ingredients from the recipe is
        # present in the available, if its not, the ingredient is 
        # not available and you cannot make any cake
        if ingredients in available:
            # This calculates how many whole cakes you could make with the available
            # amount of that ingredient
            # it divides the amount available of available ingridients by
            # the an=mount needed for one cake
            num_cakes.append(available[ingredients] // amount)
        # it returns 0 if ingridients is not available
        else:
            return 0
    # after checking all ingridients, the function returns the smallest number in the
    #  num_cakes list This is the maximum number of cakes that can be made, as it is
    #  determined by the ingredient that is in shortest supply.
    return min(num_cakes)
        
            

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})) #2