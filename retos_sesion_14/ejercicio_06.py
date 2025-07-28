#Crear una función que reciba una lista de números y devuelva una lista con los números pares y otra lista con los números impares
def separar_pares_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(numeros)
print("Pares:", pares)
print("Impares:", impares)