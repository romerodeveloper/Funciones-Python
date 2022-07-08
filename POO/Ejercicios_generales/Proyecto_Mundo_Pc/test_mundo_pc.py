from computadora import * 
from monitor import * 
from teclado import * 
from raton import * 
from orden import *


raton = Raton('USB', 'HP')
teclado = Teclado('USB', 'ACER')
monitor = Monitor('DELL', 15)
computadora1 = Computadora("HP", monitor, teclado, raton)

raton1 = Raton('COAXIAL', 'HP')
teclado1 = Teclado('USB', 'HP')
monitor1 = Monitor('TOSHIBA', 18)
computadora2 = Computadora("DELL", monitor1, teclado1, raton1)

computadoras = [computadora1, computadora2]
orden1 = Orden(computadoras)

print(orden1)