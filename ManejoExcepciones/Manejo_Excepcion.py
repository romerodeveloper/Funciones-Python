from NumerosIdenticosException import *

resultado = None

try:
    a = int(input("Ingrese un numero:"))
    b = int(input("Ingrese un numero:"))
    if a==b:
        raise NumerosIdenticosException("numeros identicos")
    resultado = a/b
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')

print("resultado: ",resultado)
    