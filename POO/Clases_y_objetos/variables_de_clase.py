#Uso de variables de clase

class Miclase:
    variables_clase = 'Valor Variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

#Impresion de variable de clase
print(Miclase.variables_clase)

#Impresion de variable de objeto
miclase = Miclase("Valor de variable de instancia")
print(miclase.variable_instancia)

#Creacion de una variable de clase al vuelo, lo que significa que al crear un objeto tambien tendra esta variable
Miclase.variables_clase2 = "Segunda variable de clase"
print(Miclase.variables_clase2)
