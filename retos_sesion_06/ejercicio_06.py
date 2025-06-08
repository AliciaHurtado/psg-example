#¿El cubo de 300 se encuentra en el siguiente rango? [N > 0 & N < 27_000_000]
n = 300
cubo = n ** 3  # elevamos al cubo

# Verificamos si el cubo está dentro del rango
en_rango = 0 < cubo < 27_000_000

print(f"Cubo de {n}:", cubo)
print("¿Está en el rango (0, 27_000_000)?", en_rango)