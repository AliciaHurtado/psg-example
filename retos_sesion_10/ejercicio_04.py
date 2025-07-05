#Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. A continuación tienes los postres que han ido pidiendo en cada salida:
print("Método intersection()")
print("Función len()")

# Postres de cada uno
jane = ["Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"]
jhon = ["Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"]

# Convertimos a conjuntos
conjunto_jane = set(jane)
conjunto_jhon = set(jhon)

# Intersección
comunes = conjunto_jane & conjunto_jhon
print("Postres en común:", comunes)

# Cálculo de compatibilidad
total = len(conjunto_jane | conjunto_jhon)
coinciden = len(comunes)
porcentaje = (coinciden / total) * 100

print("Compatibilidad:", porcentaje, "%")

if porcentaje > 50:
    print("Son compatibles 💘")
else:
    print("Tal vez deban replantear la relación 💔")
