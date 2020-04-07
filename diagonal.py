
def diagonal(array, side_1, side_2, reverse=False):
    if reverse == True:
        for a in array:
            array.append(a[::-1])
            
        array = array[::-1]
    
    print(array)

diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2, True)
