#La sobrecarga de operadores trata de modificar la funcion principal del operador, modificando su accion.
#Se subreescribe el metodo especial para poder realizar la operacion que se requiere.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Sobrecarga del metodo suma
    def __add__(self, otro):
        return f'{self.nombre} {otro.nombre}'

#Sobrecarga del metodo res
    def __sub__(self, otro):
        return self.edad - otro.edad

persona1 = Persona("Juan", 28)
persona2 = Persona("Carlos", 50)
print(persona1 + persona2)
print(persona1 - persona2)

#objeto1 + objeto2
#objeto1.__add__(objeto2)