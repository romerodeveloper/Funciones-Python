import copy
#Superclase
from math import prod


class Producto:
    def __init__(self, ref, nombre, pvp, descripcion):
        self.ref = ref
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return f"Referencia: {self.ref},\n Nombre: {self.nombre},\n Precio: {self.pvp},\n Descripcion: {self.descripcion}"

#Subclase, como parametro lleva el nombre de la superclase
class Combo(Producto):
    pass
#Subclase
class Alimento(Producto):
    marca = ""
    categoria = ""

    def __str__(self):
        return f"Referencia: {self.ref},\n Nombre: {self.nombre},\n Precio: {self.pvp},\n Descripcion: {self.descripcion},\n Marca: {self.marca},\n Categoria: {self.categoria}"
#Subclase
class Ropa(Producto):
    marca = ""
    categoria = ""
    talla = ""

    def __str__(self):
        return f"Referencia: {self.ref},\n Nombre: {self.nombre},\n Precio: {self.pvp},\n Descripcion: {self.descripcion},\n Marca: {self.marca},\n Categoria: {self.categoria},\n Talla: {self.talla}"

#Ejemplo con subclase combo
combo_1 = Combo("70010", "Combo 1", 150, "Harina de maiz (1Kg), Carne de res (2Kg), Detergente para ropa (500g)")

#Ejemplo con subclase alimento
harina = Alimento(10001, "Harina de maiz", 0.9, "Harina precocida (1Kg)")
harina.marca = "Nestle"
harina.categoria = "Cereales"

#Ejemplo con subclase Ropa
pantalon = Ropa(20001, "Pantalon", 4.7, "Stretch Color Rojo")
pantalon.marca = "Levis"
pantalon.categoria = "Dama"
pantalon.talla = 30

#Ejemplo polimorfismo
productos = [combo_1, harina]
productos.append(pantalon)
#lectura de productos
for p in productos:
    print(p.ref, p.nombre) 
#mostrar marca de productos, aunque algunos no tienen marca
'''
for p in productos:
    print(p.marca)
'''
#Uso de metodo isinstance() sirve para determinar si una variable pertence a una clase
#print(isinstance(combo_1, Combo))
#Asi se lidia con elemento de distintos atributos
for p in productos:
    if (isinstance(p, Combo)):
        print(p.ref, p.nombre)
    elif (isinstance(p, Ropa)):
        print(p.ref, p.nombre, p.talla)
    elif (isinstance(p, Alimento)):
        print(p.ref, p.nombre, p.marca)     

def descuento(p,rebaja): #Funcion que devuelve un producto conun descuento en el precio
    p.pvp= p.pvp-(p.pvp*(rebaja/100))
    return p

pantalon_desc = descuento(pantalon, 20)
print(pantalon_desc)

#Para realizar un cambio en un objeto sin que este se replique en los demas
copia_pant = copy.copy(pantalon)
copia_pant.pvp= 500
print(copia_pant)
print(pantalon)