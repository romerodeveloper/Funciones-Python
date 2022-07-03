#clase que herede atributos de varias superclases

class A:
    def __init__(self):
        print("Soy la clase A")
    def metodo_a(self):
        print("Este metodo lo hereda de a")

class B:
    def __init__(self):
        print("Soy la clase B")
    def metodo_b(self):
        print("Este metodo lo hereda de b")

class C(A,B):
    def metodo_c(self):
        print("Este metodo lo hereda de c")

#No se requiere de enviar argumentos debido a que no tienen variables definidas
objeto_3 = C()
objeto_3.metodo_a()
objeto_3.metodo_b()
objeto_3.metodo_c()