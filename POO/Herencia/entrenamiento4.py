'''
Crear un programa con tres clases Universidad, con atributos
nombre (Donde se almacena el nombre de la Universidad). 
Otra llamada Carerra, con los atributos especialidad 
(En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su 
nombre y edad. El programa debe imprimir la especialidad, edad, 
nombre y universidad de dicho estudiante con un objeto llamado persona.
'''

class Universidad:
    def __init__(self, nombre_uni):
        self.nombre_uni = nombre_uni
    
    def __str__(self) -> str:
        return f'Pertenece a la {self.nombre_uni}'

class Carrera(Universidad):
    def __init__(self, nombre_uni, nombre_c):
        super().__init__(nombre_uni)
        self.nombre_c = nombre_c
    def __str__(self) -> str:
        return  Universidad.__str__(self) + f' y estudia la carrera {self.nombre_c}'

class Estudiante(Carrera):
    def __init__(self, nombre_uni, nombre_c, nombre_est, edad):
        super().__init__(nombre_uni, nombre_c)
        self.nombre_est = nombre_est
        self.edad = edad
    def __str__(self) -> str:
        return  Carrera.__str__(self) + f' el estudiante de nombre {self.nombre_est} y  edad {self.edad}'

persona = Estudiante("ESCUELA DE INGENIEROS", "ING SISTEMAS", "NICOLAS ROMERO", 19)
print(persona)