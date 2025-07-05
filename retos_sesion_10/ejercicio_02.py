#El dueño de una tienda de ropa deportiva ha comprado ropa formal y quiere abrir una nueva tienda que combine ambos estilos. Crea un conjunto con las prendas de ambos tipos con las listas de prendas
print("Conjunto a partir de una lista")
deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

conjunto_deportiva = set(deportiva)
conjunto_formal = set(formal)

print("Prendas deportivas:", conjunto_deportiva)
print("Prendas formales:", conjunto_formal)

print("Estilo combinado (sin duplicados):")
conjunto_combinado = conjunto_deportiva | conjunto_formal  # operador de unión
print(conjunto_combinado)