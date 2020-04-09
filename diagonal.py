
def diagonal(array, side_1 = "l", side_2 = "r", reverse=False):
    if reverse == True:
        for i, a in enumerate(array):
            array[i] = a[::-1]
        array = array[::-1]

    if side_1 == "l":
        side_1 = 0
    
    elif side_1 == "r":
        side_1 = -1
    
    else:
        raise Exception("SideError - Sides must be between quotes and be 'r' or 'l'")
    
    if side_2 == "l":
        side_2 = 0
    
    elif side_2 == "r":
        side_2 = -1
    



diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]],"nope",  reverse=True)