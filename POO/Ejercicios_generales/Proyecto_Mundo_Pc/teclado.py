from dispositivo_entrada import *

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados 
        super().__init__(tipo_entrada, marca)
        

    def __str__(self) -> str:
        return f'Teclado [id: {self._id_teclado}, tipo de entrada: {self.tipo_entrada}, marca: {self._marca}]'
