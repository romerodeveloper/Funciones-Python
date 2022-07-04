#Encapsulamiento y ejercicios de practica
#Se usa dentro de la clase, para evitar desbordamiento de memoria, reduccion de ejecuciones repetidas

class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador +=1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador +=1
    
    def cuenta(self):
        return self.__contador
#Prueba de objeta a
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())

#Prueba de objeto b
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)
