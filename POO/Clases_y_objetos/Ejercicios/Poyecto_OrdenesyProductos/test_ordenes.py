from producto import *
from orden import *

producto1 = Producto("Camisa", 100.000)
producto2 = Producto("Pantalon", 150.000)
producto3 = Producto("Calsetines", 50.000)
producto4 = Producto("Blusa", 80.000)
    
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_productos(producto3)
orden1.agregar_productos(producto4)
print(orden1)
print('Total de la orden 1:', orden1.calcular_total())
orden2 = Orden(productos2)
print(orden2)
print('Total de la orden 2:', orden2.calcular_total())