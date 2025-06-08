#Comparar los números 44 y 98 , 111 y 333 , comprobar si tienen la misma paridad ambos pares o ambos impares

def misma_paridad(a, b):
    # Devuelve True si ambos son pares o ambos impares
    return a % 2 == b % 2

# Pares a comparar
pares = [(44, 98), (111, 333)]

for a, b in pares:
    resultado = misma_paridad(a, b)
    print(f"¿{a} y {b} tienen la misma paridad?: {resultado}")