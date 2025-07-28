#Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene.
def contar_vocales(cadena):
    vocales = sum([1 for letra in cadena.lower() if letra in "aeiou"])
    return vocales

resultado = contar_vocales("Python es divertido")
print(resultado)
