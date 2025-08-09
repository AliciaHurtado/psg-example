#Crea una calculadora interactiva que solicite dos números por teclado y realice las operaciones de suma, resta, multiplicación y división. El programa debe seguir solicitando dos números hasta que se ingrese "salir". Se debe incluir el manejo de excepciones para evitar errores al ingresar datos no numéricos, al intentar dividir entre cero, o ante cualquier otro error inesperado.
# ejercicio_01.py - Calculadora interactiva con manejo de excepciones

while True:
    try:
        num1 = input("Ingrese el primer número (o 'salir'): ")
        if num1.lower() == "salir":
            break

        num2 = input("Ingrese el segundo número (o 'salir'): ")
        if num2.lower() == "salir":
            break

        # Convertir a número
        num1 = float(num1)
        num2 = float(num2)

        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicación: {num1 * num2}")
        print(f"División: {num1 / num2}")

    except ValueError:
        print("🚫 Error: Debe ingresar valores numéricos.")
    except ZeroDivisionError:
        print("🚫 Error: No se puede dividir entre cero.")
    except Exception as e:
        print("💀 Error inesperado:", e)
    else:
        print("✅ Operaciones realizadas con éxito.")
    finally:
        print("🔄 Nueva operación...\n")