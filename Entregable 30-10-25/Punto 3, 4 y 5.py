#Escribir una función que reciba dos vectores y devuelva su producto escalar.
#Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
#Escribir una función que reciba dos vectores y devuelva si son paralelos o no.

def escalar(v1, v2):
    resultado = 0
    for x in range(len(v1)):
        resultado += v1[x] * v2[x]
    return resultado

def ortogonales(v1, v2):
    return escalar(v1, v2) == 0


def paralelos(v1, v2):
    if len(v1) != len(v2):
        return False
    relacion = v2[0] / v1[0]
    for i in range(1, len(v1)):
        if v1[i] == 0 and v2[i] == 0:
            continue
        elif v1[i] == 0 or v2[i] == 0:
            return False
        elif v2[i] / v1[i] != relacion:
            return False
    return True

v1 = [2, 4, 6]
v2 = [1, 2, 3]
v3 = [3, -6, 0]

print("Producto escalar:", escalar(v1, v2))
print("¿Son ortogonales?", ortogonales(v1, v3))
print("¿Son paralelos?", paralelos(v1, v2))

