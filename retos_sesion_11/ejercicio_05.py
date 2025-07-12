#Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
# Crear el diccionario del arca
arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}

# Añadir 3 especies más usando update()
arca.update({
    "🦓": 2,
    "🐘": 2,
    "🦜": 2
})

# Iterar el diccionario para mostrar animales en el arca
for animal in arca:
    print("Animal en el arca:", animal)

# ¿Existe el dragón? 🐲
existe_dragon = "🐲" in arca
print("¿Está el dragón 🐲 en el arca?:", existe_dragon)

# Eliminar la especie unicornio 🦄
del arca["🦄"]

# Modificar el valor de la especie jirafa 🦒 a 2
arca["🦒"] = 2

# Vaciar el arca después del diluvio
arca.clear()

# Mostrar el estado final del arca
print("Arca después del diluvio:", arca)