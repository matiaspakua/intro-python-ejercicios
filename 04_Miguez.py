nombre_archivo = "../intro-python-IB/data/elementos.dat"

def leer_archivo(nombre):
    """
    Funcion que leer la ruta de un archivo por parámetro y crear
    un diccionario donde, la clave es el símbolo del elemento y el
    valor de cada clave es un diccionario, con todas las propiedades
    del elemento.
    """
    elemento_dict = {}
    with open(nombre) as f:
        s = f.read()
        elemento = {}
        elemento_key = ''
        for line in s.splitlines():
            try:
                k,v = line.split("=")
                k = k.strip()   #elimino los espacios en blanco.
                v = v.strip()
                
                if k.count('Mass') | k.count('Weight') | k.count('Isotopic'):
                    if v.endswith(')'):
                        value = v.split('(')
                        v = float(value[0])
                    else:
                        v = float(v)
                
                elemento[k] = v
                if 'Atomic Symbol' in k:
                    elemento_key = elemento['Atomic Symbol']
            except:
                elemento_dict[elemento_key] = elemento
                elemento = {}
                #linea en blanco es ignorada
                continue
    return elemento_dict


def ordenar_alfabericamente(diccionario, reverse=False):
    """
    Funcion que recibe un diccionario como parámetros y escribe en un
    string el contenido del diccionario, ordenado alfabeticamente
    por la KEY del mismo y devuelve el string resultante.
    """
    keys = list(diccionario.keys())
    keys.sort(reverse=reverse)
    dict_to_string = "\n"
    for k in keys:
        elemento = diccionario[k]
        
        dict_to_string += "Elemento: " + k + "\n"
        
        for sub_keys, value in elemento.items():
            
            if "Atomic Number" in sub_keys:
                dict_to_string += "S= " + value + "\n"
            elif "Atomic Symbol" in sub_keys:
                dict_to_string += "Z= " + value + "\n"
            elif "Mass Number" in sub_keys:
                dict_to_string += "A= " + str(value) + "\n"
            elif "Relative Atomic Mass" in sub_keys:
                dict_to_string += "Masa= {:.5f} \n".format(value)
            elif "Isotopic Composition" in sub_keys:
                dict_to_string += "Abundancia= {:.5f} \n".format(value)
            elif "Standard Atomic Weight" in sub_keys:
                dict_to_string += "Masa Promedio= {:.5f} \n".format(value)
        dict_to_string += "\n"
    return dict_to_string

def agregar_a_archivo(nombre_archivo, texto):
    """
    Función que recibe un nombre de archivo y un string y 
    escribe el string en el archivo dado.
    """
    with open(nombre_archivo, 'w') as f:
        written = f.write(texto + '\n')
        
    with open(nombre_archivo) as f:
        print(f.read())
        
    
elemento_dict = leer_archivo(nombre_archivo)
elementos = ordenar_alfabericamente(elemento_dict)
#elementos = ordenar_alfabericamente(elemento_dict, True)
agregar_a_archivo("Elementos_formateado.dat", elementos)