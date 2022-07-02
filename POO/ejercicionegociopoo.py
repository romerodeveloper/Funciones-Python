#Ejercicio donde Se realizara el inventario de un negocio usando programacion orientada a objetos
# el programa debe permitirnos mostrar o borrar los datos de cada producto apartir del codigo identificador


#Estructura para los productos
from msilib.schema import Class


class Producto:

    def __init__(self, cod, nombre, categoria, pvp):
        self.cod = cod
        self.nombre = nombre
        self.categoria = categoria
        self.pvp = pvp
    
    def __str__(self):
        return 'redefinimos el str {} {}'.format(self.nombre, self.pvp)

#Y otra estructura para los negocios

class Negocio:

    def __init__(self, productos=[]):
        self.productos = productos

    def mostrar_producto(self, cod=None):
        for producto in self.productos:
            if producto.cod == cod:
                return print('{} {}'.format(producto.nombre,producto.pvp))
            print('producto no encontrado')

    def borrar_producto(self, cod=None):
        for indice, producto in enumerate(self.productos):
            if producto.cod == cod:
                del(self.productos[indice])
                return print(producto.nombre, 'Eliminado')
            print('producto no encontrado')

limones = Producto(10001, "limones", "Frutas", 0.8)
platos = Producto(10020, "Platos Alpina", "Vajilla", 2.4)

negocio = Negocio([limones, platos])
negocio.mostrar_producto(10001)
negocio.borrar_producto(10001)