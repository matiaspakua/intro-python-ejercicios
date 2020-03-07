import argparse

"""
Constantes con valores iniciales.
"""
GRAVEDAD = 9.8			#m/s2
VELOCIDAD_INICIAL = 0	#m/s
ALTURA_INICIAL = 1000	#m
N_DATOS = 100			# cantidad de datos a calcular
INSTANTE_INICIAL = 0	# ???
TIEMPO_FINAL = 0		# ??? 

parser = argparse.ArgumentParser(description='Clase para calcular caida libre.')
parser.add_argument('-vel', '--velocidad', action=store, dest='VELOCIDAD_INICIAL', default=0)
args = parser.parse_args()

def set_velocidad_inicial(vel: int):
	pass

def set_altura_inicial(alt:int):
	pass

def set_gravedad_inicial(grav:float):
	pass

def set_nombre_archivo(nombre:str):
	pass

def set_n_datos_calcular(n_datos:int):
	pass