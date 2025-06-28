# Crear una lista de 10 nombres
personas = ["Ana", "Luis", "Pedro", "María", "José", "Carmen", "Lucas", "Diego", "Sara", "Valeria"]

# Obtener una sublista de índice 5 a 9 con saltos de 2 en 2
sublista = personas[5:10:2]
print("Sublista de índice 5 a 9 con saltos de 2 en 2:", sublista)

# Verificar si "José" está en la lista original
existe_jose = "José" in personas
print("¿'José' está en la lista original?:", existe_jose)

# Ordenar la sublista alfabéticamente (A-Z)
sublista_ordenada = sorted(sublista)
print("Sublista ordenada alfabéticamente A-Z:", sublista_ordenada)

# Ordenar la lista original en orden alfabético descendente (Z-A)
personas.sort(reverse=True)