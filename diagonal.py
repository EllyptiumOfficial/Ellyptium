def diagonal(array, startSide = "ul", reverse=False):

    if type(array) != list:
        raise TypeError(f"You must enter a list, not a {type(array)}")

    try:
        l = len(array)
    
        for a in array:
            if l != len(a):
                raise IndexError("Square must be n x n")

    except TypeError:
        return print("TypeError: The list must have more than one element")

    if reverse == True:
        for i, a in enumerate(array):
            array[i] = a[::-1]
        array = array[::-1]
    
    if startSide != "l" and startSide != "r":
        raise ValueError("startSide parameter must be between quotes and be 'r' or 'l'")

    if startSide == "l":
        pass