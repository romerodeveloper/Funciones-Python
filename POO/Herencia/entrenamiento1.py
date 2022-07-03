#Herencia de vehiculos

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"El vehiculo tiene color: {self.color}, ruedas: {self.ruedas} "
    
class Carro(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self):
        return Vehiculo.__str__(self)+ f" con velocidad de {self.velocidad} Km/h, con un cilindraje {self.cilindraje}"

class Camioneta(Carro):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga
    def _str__(self):
        return Camioneta.__str__(self) + f" con una carga de {self.carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + f"de tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    def __str__(self):
        return Bicicleta.__str__(self) +f"con velocidad {self.velocidad} Km/h y cilindraje {self.cilindraje}"

def catalogar(vehiculos, ruedas=None):
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador +=1
        print(f"Se ha encontrado {contador} con {ruedas}")
        
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)

vehiculos = [
    Carro("Azul", 4, 150, 1200),
    Camioneta("Blanco", 4,100, 1300, 1500),
    Bicicleta("Verde", 2, "Urbana"),
    Motocicleta("Negro", 2, "Deportiva", 180, 900)
]

#catalogar(vehiculos)
#catalogar(vehiculos, 0)
#catalogar(vehiculos, 2)
catalogar(vehiculos, 4)