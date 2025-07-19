#Una tienda ofrece descuentos a sus clientes, si el cliente tiene una edad mayor a 60 años y tiene una compra mayor a 1000, se le aplica un descuento del 20%, si el cliente tiene una edad entre 18 y 60 años y tiene una compra mayor a 500 se le aplica un descuento del 10%, si no cumple ninguna condición se le aplica un descuento del 2%
# Solicita edad y monto de compra
edad = int(input("Ingrese su edad: "))
compra = float(input("Ingrese el monto de su compra: "))

# Aplica el descuento según condiciones
if edad > 60 and compra > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and compra > 500:
    descuento = 0.10
else:
    descuento = 0.02

# Calcula el total con descuento
monto_descuento = compra * descuento
total = compra - monto_descuento

# Muestra resultados
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total a pagar: {total}")