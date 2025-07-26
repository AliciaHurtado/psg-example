#Crea un ciclo infinito que reciba un número por teclado y verifique si el número es múltiplo de 7. La ejecución termina si se ingresa el número 0
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    if numero % 7 == 0:
        print("Es múltiplo de 7")
    else:
        print("No es múltiplo de 7")