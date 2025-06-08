
def es_palindromo(cadena):
    # Quitar espacios y convertir todo a minúsculas
    cadena_limpia = cadena.replace(" ", "").lower()
    # Verificar si es igual a su reverso
    return cadena_limpia == cadena_limpia[::-1]

# Entrada del usuario
texto = input("Ingrese una cadena: ")

# Resultado
if es_palindromo(texto):
    print("Verdadero")
else:
    print("Falso")
