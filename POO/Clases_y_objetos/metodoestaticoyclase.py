#Uso de metodo estatico

class Miclase:
    variables_clase = 'Valor Variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
    #metodo estatico
    @staticmethod
    def metodo_estatico_ejemplo():
        print(Miclase.variables_clase)

    #Metodo de clase
    @classmethod
    def metodo_clase_ejemplo(cls):
        print(cls.variables_clase)

    #Metodo de instancia
    def metodo_instancia_ejemplo(self):
        self.metodo_clase_ejemplo()
        self.metodo_estatico_ejemplo()
        print(self.variable_instancia)
        print(self.variables_clase)

Miclase.metodo_clase_ejemplo()
miobjeto1 = Miclase("Variable instancia")
miobjeto1.metodo_clase_ejemplo()
#Pueba de metodo de instancia
miobjeto1.metodo_instancia_ejemplo()