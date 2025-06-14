# Tupla con las notas del semestre
notas = (10, 61, 0, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Mostrar el promedio
print("Promedio del estudiante:", promedio)

# Verificar si aprobó
if promedio >= 51:
    print("¡Aprobó el semestre! ") 
else:
    print("No aprobó el semestre ")