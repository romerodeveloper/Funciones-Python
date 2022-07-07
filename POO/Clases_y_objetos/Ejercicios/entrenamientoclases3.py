#Ejercicio donde cada objeto de tipo persona, tendra un identificador unico

class Persona():
    contador_personas = 0

    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan', 28)
persona2 = Persona('Nicolas', 18)
print(persona1)
print(persona2)
#Con guion al piso evitemos que se use el metodo de forma externa sin crear un nuevo objeto
#persona1._generar_siguiente_valor()
persona3 = Persona('Camila', 21)
print(persona3)

        