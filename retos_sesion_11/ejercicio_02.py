# Diccionario inicial de alimentos
alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
print(alimentos)

# Añadir 4 alimentos más con update(clave=valor)
alimentos.update(pescado=["gato", "perro"])
alimentos.update(heno=["conejo"])
alimentos.update(leche=["gato"])
alimentos.update(pan=["perro"])
print(alimentos)

# Verificar si 'trigo' está en el diccionario
existe_trigo = 'trigo' in alimentos
print("¿Existe 'trigo'?", existe_trigo)

# Eliminar 'zanahoria' del diccionario
del alimentos['zanahoria']
print(alimentos)

# Crear diccionario con tupla de especies
tupla = (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))
especies = dict(tupla)
print(especies)

# Obtener y eliminar la clave 'aves'
aves = especies.pop('aves')
print("Aves eliminadas:", aves)
print(especies)

# Modificar el valor de 'felino'
especies['felino'] = '🐈'
print(especies)

# Cambiar la clave 'canino' por 'caninos' y su valor por lista
especies['caninos'] = ['🐶', '🐕']
del especies['canino']
print(especies)

# Diccionario de hábitats en peligro
habitats_peligro = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}
print(habitats_peligro)
