#IMPORT BLOCK
import serial.tools.list_ports
from time import sleep

#CONST BLOCK
MACETA_PEQUENA_HUMEDAD = 20
MACETA_MEDIANA_HUMEDAD = 30
MACETA_GRANDE_HUMEDAD = 50

#CLASS BLOCK

#CLASE MAESTRA PARA CONTROL DE HUMEDAD
class ControladorHumedadMaceta:    
    def __init__(self, numero_maceta, humedad_maxima, humedad_minima, humedad_actual):
        self.numero_maceta = numero_maceta
        self.humedad_maxima = humedad_maxima
        self.humedad_minima = humedad_minima
        self.humedad_actual = humedad_actual

#HERENCIA
class ControladorHumedadMacetaPequena(ControladorHumedadMaceta):
    def __init__(self, numero_maceta, humedad_maxima, humedad_minima, humedad_actual):
        super().__init__(numero_maceta, humedad_maxima, humedad_minima, humedad_actual)
        

class ControladorHumedadMacetaMediana(ControladorHumedadMaceta):
    def __init__(self, numero_maceta, humedad_maxima, humedad_minima, humedad_actual):
        super().__init__(numero_maceta, humedad_maxima, humedad_minima, humedad_actual)
        

class ControladorHumedadMacetaGrande(ControladorHumedadMaceta):
    def __init__(self, numero_maceta, humedad_maxima, humedad_minima, humedad_actual):
        super().__init__(numero_maceta, humedad_maxima, humedad_minima, humedad_actual)
        
# Variables temporales. La maceta queda definida en función de su
# controlador de humedad

#Numero de maceta
n_x = 1
n_y = 2
n_z = 3

#Humedad actual
lectura_sensor_humedad = serial.tools.list_ports.comports()
serialInst = serial.Serial()
lista_lecturas = []

#Extraccion en variables separadas
for lectura in lectura_sensor_humedad:
    lista_lecturas.append(int(lectura))
    sleep(3600)

#Prueba
maceta_hibisco = ControladorHumedadMacetaPequena(n_x, 100, MACETA_PEQUENA_HUMEDAD, lista_lecturas[0])
maceta_palmera = ControladorHumedadMacetaMediana(n_y, 150, MACETA_MEDIANA_HUMEDAD, lista_lecturas[1])
maceta_tomate = ControladorHumedadMacetaGrande(n_z, 200, MACETA_GRANDE_HUMEDAD, lista_lecturas[2])

#Bloque lógico
if maceta_hibisco.humedad_minima >= maceta_hibisco.humedad_actual:
    print(f'Hibisco necesita agua => {maceta_hibisco.humedad_actual}')
    
if maceta_palmera.humedad_minima >= maceta_palmera.humedad_actual:
    print(f'Palmera necesita agua => {maceta_palmera.humedad_actual}')
    
if maceta_tomate.humedad_minima >= maceta_tomate.humedad_actual:
    print(f'Tomates necesitan agua => {maceta_tomate.humedad_actual}')