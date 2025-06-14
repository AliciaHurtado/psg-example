# Ingresar una pregunta por teclado
texto = input("Escribe una pregunta: ")

# Almacenar en una tupla
pregunta = (texto,)

# Concatenar las tuplas
pregunta_formateada = ('¿',) + pregunta + ('?',)

# Imprimir la tupla concatenada
print("Pregunta con signos:", pregunta_formateada)

# Repetir la tupla dos veces
pregunta_repetida = pregunta_formateada * 2
print("Pregunta repetida:", pregunta_repetida)