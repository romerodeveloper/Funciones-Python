#Uso de funciones lambda

#Forma tradicional de una funcion
def doblar(num):
    resultado = num*2
    return resultado
doblar(10)

#Funcion reducida, se reduce una linea de codigo
def doblar2(num):
    return num*2
doblar2(20)

#Funcion aun mas reducida
def doblar3(num): return num*2
doblar3(30)

#Funcion lamda es mas eficiente debido a que reduce codigo y no requiere de ser nombrada. nos ahorra el uso de def
doblar4 = lambda num: num*2
doblar4(5)

#ejemplo 
revertir = lambda cadena: cadena[::-1]
print(revertir("cadena"))
