#Escribir una función que reciba un vector y devuelva su norma.
def norma(v):
    return (sum(x ** 2 for x in v)) ** 0.5

vector = [3, 4]
resultado = norma(vector)

print("Vector:", vector)
print("Norma del vector:", resultado)
