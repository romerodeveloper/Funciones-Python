#Objetos dentro de objetos

class Videojuego:
#Metodo constructor de clase
    #Constructor de clase
    def __init__(self, titulo, genero, lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self.lanzamiento = lanzamiento
        print("se creo el video juego: ", self.titulo)

    #Redefinir el metodo string
    def __str__(self): 
        return f"{self.titulo}  {self.lanzamiento}"

class Catalogo:
    vjuegos = []
    def __init__(self, vjuegos=[]):
        self.vjuegos = vjuegos
    
    def agregar(self, v):
        self.vjuegos.append(v)

    def mostrar(self):
        for v in self.vjuegos:
            print(v)

vj = Videojuego("the last of us", "accion", 2012)
vj2 = Videojuego("gta v", "accion", 2013)
#c = Video("Black panther", 134, 2018)
productos = Catalogo(vjuegos=[vj, vj2])

productos.agregar(Videojuego("pokemos", "rpg", 1996))
productos.mostrar()