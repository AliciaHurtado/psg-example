#Jhon colecciona autos a escala 1:64, tiene los siguientes autos. Jess tambien colecciona autos a escala 1:64, tiene los siguientes autos ¿Que autos tienen en común ambos coleccionistas?, ¿Cuáles son los autos en común?
# Autos de Jhon y Jess
autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

# Autos en común
autos_comunes = autos_jhon.intersection(autos_jess)

# Verificación y resultado
if autos_comunes:
    print("Tienen autos en común.")
    print(f"Autos en común: {autos_comunes}")
else:
    print("No tienen autos en común.")