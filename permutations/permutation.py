from itertools import permutations

def get_permutations(s):
    # generate all permutation of strings s
    perm = permutations(s)    
    # Convert permutations into strings and add to a set
    # to remove duplicates
    unique_perm_set = set(''.join(p) for p in perm)
    print(unique_perm_set)
    
    # convert the set back into a list
    unique_perm_list = list(unique_perm_set)
    print(unique_perm_list)
    
    return unique_perm_list

print(get_permutations("abc"))