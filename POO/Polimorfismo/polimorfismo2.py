#ejemplo dos de poliformismo

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("yo hago guaooo!")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guao")
perro.hablar()

animale = Animales("Miau")
animale.hablar()