from empleado import *
from gerente import *

def imprimir_detalles(objeto):
    print(objeto.mostrar_detalles())
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("Juan", 5000)
imprimir_detalles(empleado)

gerente = Gerente("Karla", 6000, "Sistemas")
imprimir_detalles(gerente)
