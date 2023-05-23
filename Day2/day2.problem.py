def filter_list(list):
    'return a new list with the strings filtered out'
    return[L for L in list if not isinstance(L, str)]
