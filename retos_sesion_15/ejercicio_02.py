#Crea un programa que permita construir una canasta de frutas solicitando ingresar frutas por teclado, una por una, y almacenándolas en una lista. El programa debe finalizar cuando se ingrese "salir".
# Definir excepción personalizada
class FrutaInvalidaError(Exception):
    pass

# Lista de frutas permitidas
frutas_permitidas = ['🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍑']
canasta = []

while True:
    try:
        fruta = input("Ingrese una fruta (o 'salir'): ")
        if fruta.lower() == "salir":
            break

        if fruta not in frutas_permitidas:
            raise FrutaInvalidaError("La fruta no está permitida.")

        canasta.append(fruta)

    except FrutaInvalidaError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error inesperado:", e)
    else:
        print("✅ Fruta agregada a la canasta.")
    finally:
        print("Canasta actual:", canasta)
        print("-----")