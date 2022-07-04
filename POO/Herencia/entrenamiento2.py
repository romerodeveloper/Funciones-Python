'''
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. Definir los
métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
con el resultado de la nota y si ha aprobado o no.
'''
class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def aprobo(self):
        if self.nota > 3.0:
            return 'Aprobo'
        else:
            return 'No aprobo'
    
    def __str__(self):
        return f'El estudiante {self.nombre}, con una nota de {self.nota}, {self.aprobo()}'

estudiante = Estudiante("Nicolas romero", 5.0)
print(estudiante)

estudiante2 = Estudiante("Emanuel romero", 2.0)
print(estudiante2)