from errors import launch_error

def build_triangle(num):
    
    triangle = []
    for r in range(num):
        row = []
        for k in range(r+1):
            try:
                if k == 0:
                    raise IndexError
                row.append(triangle[r-1][k-1] + triangle[r-1][k])
            
            except IndexError:
                row.append(1)
            
        triangle.append(row) 
    
    return triangle


def pascal_triangle(num, mode="default"):

    launch_error("ERROR: YO MEN, what r u doing? The triangle must be positive!","Your input: {}".format(num))

    lista = [1]

    if mode == "default":
        return build_triangle(num)
    
    elif mode == "maxnum":

        while num > sum(lista):
            lista.append(lista[-1]*2)
    
        return build_triangle(len(lista))
    
    else:
        launch_error("ERROR: YO MEN, The modes are 'default' and 'maxnum'")