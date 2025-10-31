# Escribir una función poker que reciba cinco cartas de la baraja e informe si esas cartas forman o no un poker (es decir que hay 4 cartas con el mismo número).
def poker(cartas): 
    numeros = [carta[0] for carta in cartas]
    frecuencias = {}
    for numero in numeros:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1

    for cuenta in frecuencias.values():
        if cuenta == 4:
            return True
    return False