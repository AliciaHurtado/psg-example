#Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo. La ejecución termina si la frase ingresada contiene la palabra salir
while True:
    frase = input("Ingresa una frase (o escribe 'salir' para terminar): ").lower()
    
    if "salir" in frase:
        print("¡Hasta luego!")
        break

    frase_sin_espacios = ''.join(frase.split())
    if frase_sin_espacios == frase_sin_espacios[::-1]:
        print("La frase es un palíndromo.")
    else:
        print("La frase NO es un palíndromo.")