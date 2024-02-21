def sum_n(items, n):
    """Returns the sum of first n items in an array,
    
    Args:
        items(array): list or array-like object
        n (int): number of items to in the array to sum
    Return:
        int: sum of the first n items
    """

    sum = 0
    for i in range(n-1):
        sum += items[i]
    
    return sum 
