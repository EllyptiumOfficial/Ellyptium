from math import factorial, sqrt

def wilsqmix(n):                                            # DEFINICIÓN DE FUNCIÓN WILSQMIX()

    if n%2 == 0 and n != 2:                                 #Lista de primeros números primos (más comunes)
        return False
    
    if n%3 == 0 and n != 3:
        return False
    
    if n%5 == 0 and n != 5:
        return False
    
    if n%7 == 0 and n != 7:
        return False
    
    if n%11 == 0 and n != 11:
        return False

    for a in range(2, int(sqrt(n))):                        #FORMULA PRINCIPAL. En caso de método instantáneo, se usa el factorial
        if (factorial(a-1)+1) % a == 0:                     #Si el módulo de el número con cualquier número primo anterior a la raíz de este
            if n%a == 0:                                    #entonces el número es primo. Este es el método más "efectivo".
                return False
    
    return True

def is_prime(n, method = "inst"):                           #DEFINICIÓN DE FUNCIÓN IS_PRIME()

    if method == "inst":                                    #Método instantáneo, usa función wilsqmix()

        return wilsqmix(n)


#_______________________________________________________________________________
# No es necesario mirar esta parte del código. Se quedó obsoleta durante su desarrollo y se piensa completarla
# Is not neccesary to look at this part of the code. This part is going to be finished but not today
# ______________________________________________________________________________        
    
#    elif method == "DB":                                    #Método base de datos
#
#        primefile = open("primes.txt", "r")                 #Abre el archivo
#
#        firstline = int(primefile.readline())
#
#        if n < firstline:                                   #Si número menor que el máximo del archivo
#            while True:
#                try:                                        #Try para evitar un desbordamiento         
#                    read = int(primefile.readline())        #Se lee la 1ª línea
#
#                    if read == n:                           #Se compara el número, en caso de igual, es primo
#                        primefile.close()                   #SIEMPRE -- Cerrar archivo
#                        return True
#                    
#                    elif read > n:                          #En el momento que los primos son mayores que el número, se descarta posibilidad
#                        primefile.close()                   #SIEMPRE -- Cerrar archivo
#                        return False
#                
#                except:
#                    return False                            #Except del try, evita desboradamiento
#        
#        elif n == firstline:
#            return True
#        
#        else:
#            if sqrt(n) <= firstline:
#                pass