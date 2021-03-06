import operator
from functools import reduce
from math import prod
from os import sys

def launch_error(*args):
    try:
        raise Exception

    except Exception:
        lines = ""
        for a in args:
            lines += a
            lines += "\n"
        
        print(lines)
        sys.exit()

def diagonal(array, startSide = "l", mode = "ret", reverse=False):

    modes = ["ret", "sum", "sub", "mult"]

    if mode != "ret":
        if mode not in modes:
            launch_error("Avaliable modes are:\n\tSimple return: 'ret'\n\tSumatory: 'sum'\n\tSubstraction: 'sub'\n\tMultiply: 'mult'")



    if type(array) != list:
        launch_error(f"You must enter a list, not a {type(array)}")

    try:
        l = len(array)
    
        for a in array:
            if l != len(a):
                launch_error("Square must be n x n")

    except IndexError:
        return print("The list must have more than one element")    
    
    if startSide != "l" and startSide != "r":
        launch_error(f"Valid starting sides are 'r' and 'l', not '{startSide}'")


    if reverse == True:
        for i, a in enumerate(array):
            array[i] = a[::-1]
        array = array[::-1]

    if startSide == "r":
        for i, a in enumerate(array):
            array[i] = a[::-1]
    
    diagonalvalues = []

    for a in range(len(array)):
        diagonalvalues.append(array[a][a])
    
    if mode == "ret":
        return diagonalvalues
    
    elif mode == "sum":
        return sum(diagonalvalues)
    
    elif mode == "sub":
        return reduce(operator.sub, diagonalvalues)

    elif mode == "mult":
        return prod(diagonalvalues)