import argparse
import numpy as np
import sys
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Programa para calcular caida libre.')

parser.add_argument('-v', '--velocidad', action='store', dest='vel', default=0, type=float)
parser.add_argument('-al', '--altura', action='store', dest='alt', default=1000, type=int)
parser.add_argument('-g', '--gravedad', action='store', dest='grav', default=9.8, type=float)
parser.add_argument('-o', '--nombre', action='store', dest='nombre', type=str)
parser.add_argument('-n', '--Ndatos', action='store', dest='N', default=100, type=int)
parser.add_argument('--ti', '--instante_inicial', action='store', dest='ti', default=0, type=int)
parser.add_argument('--tf', '--tiempo_final', action='store', dest='tf', type=int)

args = parser.parse_args()


def calcular_posicion(tn, altura_inicial, velocidad_inicial, grav):
    """
    y = h_0 + v_0.t – (1/2).g.t² (posición)
    """
    return altura_inicial + velocidad_inicial * tn - (1//2) * grav * (tn**2) 

def calcular_velocidad(tn, velocidad_inicial, grav):
    """
    v = v_0 – g.t (velocidad)
    """
    return velocidad_inicial - grav*tn

def calcular_tiempo_h0(altura_inicial, velocidad_inicial, grav):
    ti=0
    coefs=[(-0.5*grav), velocidad_inicial, altura_inicial]
    r=roots(coefs)
    if r[0]>r[1]:
        ti=r[0]
    else:
        ti=r[1]
    return ti

def verificar_valores():
    """
    --ti: No puede ser mayor que el tiempo de llegada a la posición ℎ=0
    --tf: Valor por defecto será el correspondiente al tiempo de llegada a la posición ℎ=0.
    """
    if args.tf is None:
        args.tf=calcular_tiempo_h0(args.alt, args.vel, args.grav)
    if args.ti < args.tf:
        pass
    else:
        print('ERROR: ti>tf')
        args.ti=args.tf

#if args.nombre is None:
#    np.savetxt(sys.stdout, generar_datos(), fmt='%.2e', header="# Tiempo    Altura   Velocidad", comments="% ")
#else:
#    np.savetxt(args.nombre + ".txt", generar_datos(), fmt='%.2e', header="# Tiempo    Altura   Velocidad", comments="% ")



def generar_datos():
    rango_tiempos = np.linspace(args.ti, args.tf, args.N)
    pos = calcular_posicion(rango_tiempos, args.alt, args.vel, args.grav)
    vel = calcular_velocidad(rango_tiempos, args.vel, args.grav)
    return np.array([rango_tiempos,pos,vel])

# ***************************************************************************** 

verificar_valores()
plt.plot(generar_datos())
plt.show()