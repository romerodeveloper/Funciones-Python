#Ejercicio donde Se realizara el inventario de un negocio usando programacion estructurada
# el programa debe permitirnos mostrar o borrar los datos de cada producto apartir del codigo identificador

productos = [
    {'cod' : 10001, 'Nombre' : 'Jabon Harmony', 'Categoria' : 'Higiene Personal', 'pvp' : 0.9},
    {'cod' : 10002, 'Nombre' : 'Cereal Nestle', 'Categoria' : 'Cereal', 'pvp' : 1.5},
    {'cod' : 10003, 'Nombre' : 'Limones', 'Categoria' : 'Fruta', 'pvp' : 0.7},
]

#Visualizar productos del negocio
def mostrar_producto(productos, cod):
    for producto in productos:
        if producto['cod'] == cod:
            return print('{} {}'.format(producto['Nombre'],producto['pvp']))
    print('producto no encontrado')

#mostrar_producto(productos, 10003)

def borrar_producto(produc, cod):
    for indice, producto in enumerate(produc):
        if producto['cod'] == cod:
            del(produc[indice])
            return print(producto, 'Eliminado')
    print('producto no encontrado')
borrar_producto(productos, 10002)