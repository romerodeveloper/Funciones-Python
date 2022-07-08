from dispositivo_entrada import *

class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones 
        super().__init__(tipo_entrada, marca)


    def __str__(self) -> str:
        return f'Raton [id: {self._id_raton}, tipo de entrada: {self.tipo_entrada}, marca: {self._marca}]'
