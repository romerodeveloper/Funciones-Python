#Ejemplo de herencia

#Superclase
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
#print(combo_1)

#Ejemplo con subclase alimento
harina = Alimento(10001, "Harina de maiz", 0.9, "Harina precocida (1Kg)")
harina.marca = "Nestle"
harina.categoria = "Cereales"
#print(harina)

#Ejemplo con subclase Ropa
pantalon = Ropa(20001, "Pantalon", 4.7, "Stretch Color Rojo")
pantalon.marca = "Levis"
pantalon.categoria = "Dama"
pantalon.talla = 30
print(pantalon)