print("Matias Miguez")
print("clase 2")

s = '''Aquí me pongo a cantar
Al compás de la vigüela,
Que el hombre que lo desvela
Una pena estraordinaria
Como la ave solitaria
Con el cantar se consuela.'''

# 1) distinguiendo mayusculas y minusculas: es, la, que, con y Es, La, Que, Co
smin = s.lower()

es = smin.count('es')
la = smin.count('la')
que = smin.count('que')
co = smin.count('co')

Es = s.count('Es')
La = s.count('La')
Que = s.count('Que')
Co = s.count('Co')


print("Distinguiendo {} {} {} {}".format(Es,La,Que,Co))
print("Sin distinguir {} {} {} {}".format(es,la,que,co))

# 2) Cree una lista, donde cada elemento es una línea del string s y 
# encuentre la de mayor longitud. Imprima por pantalla la línea y su longitud.
lineas = s.splitlines()
max_len = 0
max_index = 0
i = 0
for palabra in lineas:
    if len(palabra) > max_len:
        max_len = len(palabra)
        max_index = i
    i+=1
print("{} Longitud={}.".format(lineas[max_index], max_len))


# 3) Forme un nuevo string de 10 caracteres que contenga los 5 
# primeros y los 5 últimos del string anterior s. Imprima por pantalla 
# el nuevo string.

s_nuevo = s[0:5:1] + s[-5:]
print(s_nuevo)

# 4) Forme un nuevo string que contenga los 10 caracteres centrales de s 
# (utilizando un método que pueda aplicarse a otros strings también). Imprima 
# por pantalla el nuevo string.

middle = int(len(s)/2)
s_centro = s[middle-5:middle+5:1]

print(s_centro)


# 5) Cambie todas las letras "m" por "n" y todas las letras "n" por "m" 
# en s. Imprima el resultado por pantalla.

i = 0
s_reemplazado = ''
while i<len(s):
    
    if s[i] == 'm':
        s_reemplazado = s_reemplazado + 'n'
    elif s[i] == 'n':
        s_reemplazado =s_reemplazado + 'm'
    else:
        s_reemplazado =s_reemplazado + s[i]
    i+=1
print(s_reemplazado)