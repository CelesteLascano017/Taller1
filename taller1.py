import math

vector: List[int] = [2,1,5,9,3,2]
 
def serie_errorabs: 
    v_real = 2
    n = 0
    S = 0
    while True:
        i = 1 / (2**n)
        S += i    

def bubblesort(vector):
    tamano = len(vector)
    contador = 0
    for i in range (tamano):
        swapped = False
        for j in range(1, tamano -1):
            if(vector[j] < vector[j-1] ):
                vector[j], vector[j-1] = vector[j-1], vector[j]
                swapped = True
                contador += 1
        if(not swapped):
            break    
    print(f"Cambios: {contador}")    
    return vector 


def fibonacci(n):
    if (n==0):
        return 0
    else:
        x = 0
        y = 1
        for i in range(1, n-1):
            z = x + y
            x = y
            y = z
    return y