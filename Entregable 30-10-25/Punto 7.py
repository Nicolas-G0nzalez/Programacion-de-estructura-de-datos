#Dada una lista de números enteros y un entero k, escribir una función que:
#Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
#Devuelva una lista con aquellos que son múltiplos de k.

def list_nums(lista, k):
    menores = [x for x in lista if x < k]
    mayores = [x for x in lista if x > k]
    iguales = [x for x in lista if x == k]
    multiplos = [x for x in lista if x % k == 0]
    return menores, iguales, mayores, multiplos


num = list(range(101))
k_input = input("Ingrese un numero entero como referencia: ")
k = int(k_input.strip())

menores, mayores, iguales, multiplos = list_nums(num, k)

print("Lista original:", num)
print("Los numeros menores a", k, "son:", menores)
print("Los numeros mayores a", k, "son:", mayores)
print("Los numeros iguales a", k, "son:", iguales)
print("Los multiplos de", k, "son:", multiplos) 