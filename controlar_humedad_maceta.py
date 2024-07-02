#IMPORT BLOCK
import serial
import time

#Lectura de los puertos seriales de Arduino
#El puerto está vacio ya que no tengo aún Arduino
ser = serial.Serial('', 9600)
time.sleep(2)

def reading_humidity():
    linea = ser.readline().decode('utf-8').strip()
    humedad1, humedad2, humedad3 = map(int, linea.split(","))
    return humedad1, humedad2, humedad3

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
        
    def need_water(self):
        return self.humedad_actual <= self.humedad_minima

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
        
# Humedad de Arduino
humedad1, humedad2, humedad3 = reading_humidity()
value_maceta1, value_maceta2, value_maceta3 = False

#Prueba
maceta_hibisco = ControladorHumedadMacetaPequena(1, any, MACETA_PEQUENA_HUMEDAD, humedad1)
maceta_palmera = ControladorHumedadMacetaMediana(2, any, MACETA_MEDIANA_HUMEDAD, humedad2)
maceta_tomate = ControladorHumedadMacetaGrande(3, any, MACETA_GRANDE_HUMEDAD, humedad3)

#Bloque lógico
def maceta_aviso():
    if maceta_hibisco.need_water():
        print(f'Hibisco necesita agua => {maceta_hibisco.humedad_actual}')
        
    if maceta_palmera.need_water():
        print(f'Palmera necesita agua => {maceta_palmera.humedad_actual}')
        
    if maceta_tomate.need_water():
        print(f'Tomates necesitan agua => {maceta_tomate.humedad_actual}')
        

def maceta_necesita_regada():
    if maceta_hibisco.need_water():
        return value_maceta1
        
    if maceta_palmera.need_water():
        return value_maceta2
        
    if maceta_tomate.need_water():
        return value_maceta3