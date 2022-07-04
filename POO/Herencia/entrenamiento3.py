'''
Realizar un programa en el cual se declaren dos valores 
enteros por teclado utilizando el método __init__. Calcular
después la suma, resta, multiplicación y división. Utilizar
un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
'''

class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese un numero: "))
        self.num2 = int(input("Ingrese un segundo numero: "))
    def suma(self):
        return self.num1+self.num2
    def resta(self):
        return self.num1-self.num2
    def multiplicacion(self):
        return self.num1*self.num2
    def division(self):
        return self.num1/self.num2
        
operacion1 = Calculadora()
print(operacion1.multiplicacion())
print(operacion1.suma())
print(operacion1.resta())
print(operacion1.division())