# Listas iniciales
productos = ["Bon Bon Bum", "Oreo", "Chizitos", "Galleta", "Chicle"]
precios = [1.5, 2.0, 1.8, 1.2, 0.5]

# 1. Agregar 2 productos nuevos al final
productos.append("Snickers")
precios.append(2.5)

productos.append("Trululú")
precios.append(1.0)

# 2. Eliminar "Bon Bon Bum" de ambas listas
if "Bon Bon Bum" in productos:
    indice = productos.index("Bon Bon Bum")
    productos.pop(indice)
    precios.pop(indice)

# 3. ¿Cuánto cuesta "Oreo" y "Chizitos"?
precio_oreo = precios[productos.index("Oreo")]
precio_chizitos = precios[productos.index("Chizitos")]
print("Precio de Oreo:", precio_oreo)
print("Precio de Chizitos:", precio_chizitos)

# 4. Producto más caro y más barato
indice_max = precios.index(max(precios))
indice_min = precios.index(min(precios))
print("Producto más caro:", productos[indice_max], "-", precios[indice_max])
print("Producto más barato:", productos[indice_min], "-", precios[indice_min])

# 5. ¿Cuántos productos hay en total?
print("Cantidad total de productos:", len(productos))

# 6. ¿Cuánto cuestan todos los productos?
print("Suma total de precios:", sum(precios))

# 7. Ordenar productos y precios del más barato al más caro
productos_y_precios = list(zip(productos, precios))
productos_y_precios.sort(key=lambda x: x[1])  # Orden por precio

# Desempaquetar listas ordenadas
productos, precios = zip(*productos_y_precios)
productos = list(productos)
precios = list(precios)

print("Productos ordenados por precio (menor a mayor):")
for p, pr in zip(productos, precios):
    print(f"{p}: {pr}")

# 8. Eliminar todos los productos de las listas
productos.clear()
precios.clear()

print("Productos:", productos)
print("Precios:", precios)