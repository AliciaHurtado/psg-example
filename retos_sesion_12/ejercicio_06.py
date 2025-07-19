#Crea una calculadora por consola que realice las operaciones de suma, resta, multiplicación y división. Las operaciones se ingresan por teclado separadas por comas en el siguiente formato
# Solicita la operación
entrada = input("Operación (formato: num1, num2, operación): ")

# Divide la entrada
partes = entrada.split(",")

# Verifica que haya exactamente 3 partes
if len(partes) != 3:
    print("-------------")
    print("Formato incorrecto")
else:
    # Limpia espacios y convierte datos
    try:
        num1 = float(partes[0].strip())
        num2 = float(partes[1].strip())
        operacion = partes[2].strip()

        # Realiza la operación
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División entre cero"
        else:
            resultado = "Operación no válida"

        print("-------------")
        print("Resultado:", resultado)

    except ValueError:
        print("-------------")
        print("Entrada numérica inválida")