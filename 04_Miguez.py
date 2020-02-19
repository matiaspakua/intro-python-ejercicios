nombre = "../intro-python-IB/data/elementos.dat"

def leer_archivo(nombre):
    elemento_dict = {}
    with open(nombre) as f:
        s = f.read()
        elemento = {}
        for line in s.splitlines():
            try: 
                k,v = line.split("=")
                k = k.strip()   #elimino los espacios en blanco.
                if "Symbol" in k:
                    elemento_dict[]
                v = v.strip()
                elemento[k] = v
            except:
                print("linea no válida o vacia: {}".format(line))
        print(elemento)
leer_archivo(nombre)