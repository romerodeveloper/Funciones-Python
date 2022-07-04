#Mas sobre encapsulamiento
#metodo get y set

class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    #El uso del property es para poder instanciar el metodo sin requerir el uso de los parentesis
    #como si fuera una variable
    @property #get
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter #metodo set
    def cuenta(self, cuenta):
        self._cuenta = cuenta
    
    @property #get
    def contador(self):
        return self._contador

    @contador.setter  #metodo set
    def contador(self, contador):
        self._contador = contador

a = A() 
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)
a.contador = 10
print(a.contador)
        