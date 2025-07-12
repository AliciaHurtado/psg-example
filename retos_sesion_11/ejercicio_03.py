#Crea un diccionario con la siguiente tupla de especies animales
# Crear diccionario con tupla
tupla = (('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅']))
especies = dict(tupla)
print(especies)

# Obtener y eliminar la clave 'aves'
aves = especies.pop('aves')
print("Aves eliminadas:", aves)
print(especies)

# Modificar el valor de la clave 'felino'
especies['felino'] = '🐈'
print(especies)

# Cambiar clave 'canino' por 'caninos' y su valor por una lista
especies['caninos'] = ['🐶', '🐕']
del especies['canino']
print(especies)
