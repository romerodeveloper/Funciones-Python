#Ejercicios para practica de funciones 
#ejercicio de area de un rectangulo

from cmath import pi

def area_rectangulo(base, altura): return base*altura
print(f"Area de un rectangulo usando una funcion resumida: {area_rectangulo(15,10)}")

#ejercicio del area de un circulo 

Area_circulo = lambda radio: (radio**2)*pi
print(f"Area de circulo usando la funcion lambda: {Area_circulo(2.5)}")

#ejercicio de comparacion entre dos numeros, si el primer numero es mayor al segundo retornar 1
#si el primer numero es menor al segundo retornar -1, si son iguales retornar cero

def comparacion(num_1, num_2):
    if num_1 > num_2:
        return 1
    elif num_1 < num_2:
        return -1
    elif num_1 == num_2:
        return 0
print(comparacion(2,2))

#ejercicio de separacion de los valores de una lista, una lista de pares y otra de impares

def separacion(lista):
    lpar, limpar = [], []
    for numero in lista:
        if numero % 2 == 0:
            lpar.append(numero)
        else:
            limpar.append(numero)
    return lpar, limpar

pares, impares = separacion([1,2,3,22,55,4,5,6,7,8,9,10])

print(pares)
print(impares)
