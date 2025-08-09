#Crea un programa que simule el funcionamiento de un cajero automático solicitando al usuario un monto a retirar. Si el monto ingresado es mayor al saldo disponible, el programa debe lanzar una excepción personalizada que indique que no hay fondos suficientes. Además, si el monto ingresado es mayor a 1000, debe lanzarse una excepción genérica que advierta que el monto excede el límite permitido por transacción
# Definir excepción personalizada
class FondosInsuficientesError(Exception):
    pass

saldo = 5000  # Saldo inicial

while True:
    try:
        monto = input("Ingrese monto a retirar (o 'salir'): ")
        if monto.lower() == "salir":
            break

        monto = float(monto)

        if monto > saldo:
            raise FondosInsuficientesError("No hay fondos suficientes.")
        if monto > 1000:
            raise Exception("El monto excede el límite permitido por transacción.")

        saldo -= monto
        print(f"✅ Retiro exitoso. Saldo restante: {saldo}")

    except ValueError:
        print("🚫 Error: Debe ingresar un monto numérico.")
    except FondosInsuficientesError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    finally:
        print(f"💰 Saldo actual: {saldo}")
        print("-----")