#Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formaran la diagonal del rectangulo
#añade un metodo constructor para crear ambos puntos, si no se envian se definiran los de origen
#añade un metodo mostrar base
#añade un metodo mostrar altura
#añade un metodo mostrar area

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangulo:

    def __init__(self, punto1=Punto(0,0), punto2=Punto(0,0)):
        self.inicio = punto1
        self.final = punto2
        self.base = abs(self.final.x-self.inicio.x)
        self.altura = abs(self.final.y-self.inicio.y)
        self.area = self.base*self.altura

    def mostrar_base(self):
        print("la base del rectangulo es ", self.base)
    
    def mostrar_altura(self):
        print("la altura del rectangulo es ", self.altura)

    def mostrar_area(self):
        print("el area del rectangulo es ", self.area)

a = Punto(10,2)
b = Punto(3,-5)
rect = Rectangulo(a,b)
rect.mostrar_area()