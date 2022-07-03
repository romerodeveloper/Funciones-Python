#Metodos especiales
#Son utiles para redefinir funciones integradas y darles un significado segun la necesidad


class Video:
#Metodo constructor de clase
    #Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se creo el video", self.titulo)
    '''
    #Destructor de clase
    def  __del__(self):
        print("se elimino el video", self.titulo)
    '''
    #Redefinir el metodo string
    def __str__(self): 
        return f"{self.titulo} publicado en {self.lanzamiento} con una duracion de {self.duracion}"
    
    #Redefinimos el metodo len() para que retorne la duracion de la pelicula
    def __len__(self):
        return self.duracion

#v = Video("the avengers", 143, 2012)
c = Video("Black panther", 134, 2018)
print(str(c))
print(len(c))