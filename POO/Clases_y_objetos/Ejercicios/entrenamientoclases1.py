#Ejercicio de plano cartesiano
#Crear un punto recibiendo una coordenada de la forma (x,y), mostrar el punto y encontrar el cuadrante al que pertence
#Construir un vector y su distancia 

import math


class Punto:
    def __init__(self, x=None, y=None):
        if x==None and y==None:
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y
        print("Se ingreso las coordenadas")
        
    def __str__(self):
        return f"Coordenada ({self.x},{self.y})"
        
    def cuadrante(self):
        if self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante 4"
        elif self.x != 0 and self.y == 0:
            return "Se ubica sobre el y"
        elif self.x == 0 and self.y != 0:
            return "Se ubica sobre el x"
        else:
            return "Es una coordenada de (0,0)"
    
    def vector(self, p):
        print(f"El vector que une los puntos {self} y {p} es igual a ({p.x-self.x},{p.y-self.y})")

    def distancia(self, p):
        distancia = math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)
        print(f"la distancia entre los puntos {self}, y {p} es {distancia}") 

coordenada = Punto(-12,10)
d = Punto(13,23)
#print(str(coordenada))
print(coordenada.cuadrante())

coordenada.distancia(d)
        