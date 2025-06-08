#Construir el operador XNOR en Python
def xnor(a, b):
# XNOR devuelve True si ambos son iguales
 return not (a ^ b)

# Tabla de verdad de XNOR
valores = [True, False]

print("A\tB\tXNOR(A, B)")
for a in valores:
    for b in valores:
        resultado = xnor(a, b)
        print(f"{a}\t{b}\t{resultado}")