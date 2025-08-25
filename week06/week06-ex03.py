lst = [4, 1, 7, 1, 9, 2]

def manual_max(lst):
    """
    Return the maximum value in a list without using max().

    Args:
        lst (list): A list of comparable elements (e.g. numbers).

    Returns:
        The largest element in the list.

    Examples:
        >>> manual_max([1, 5, 3, 9, 2])
        9

        >>> manual_max([-10, -5, -3])
        -3
    """
    
    highest = lst[0]  

    for item in lst[1:]:
        if item > highest:
            highest = item

    return highest 

print(manual_max(lst))