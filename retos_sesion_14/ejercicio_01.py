#Crea una funcion que reciba una lista de calificaciones y devuelva el promedio de las mismas. Las calificaciones son: 50, 75, 80, 91, 70
def promedio(calificaciones):
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    return suma / cantidad

resultado = promedio([50, 75, 80, 91, 70])
print(resultado)