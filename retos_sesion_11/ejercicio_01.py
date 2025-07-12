# Diccionario con información del animal marino
animal = {
    'especie': 'Delfín nariz de botella',
    'hábitat': 'Océano tropical',
    'dieta': 'Peces pequeños y calamares',
    'estado_de_salud': 'Bueno',
    'edad': 8,
    'responsables': {'Carlos', 'Ana', 'Lucía'}
}

print(animal)
print(type(animal))

# Acceder a los responsables
print(animal['responsables'])
print(type(animal['responsables']))