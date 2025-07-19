#Tienes una app para gestionar contactos, cada contacto tiene un nombre y un número de teléfono, si el contacto tiene un número de teléfono válido (11 dígitos incluyendo el código de país) y un nombre valido se guarda en la lista de contactos y muestra el mensaje Contacto guardado, caso contrario se muestra el mensaje de error Datos incorrectos.
# Lista de contactos
contactos = []

# Solicita nombre y número
nombre = input("Nombre: ")
telefono = input("Teléfono: ")

# Validación
es_nombre_valido = bool(nombre)  # truthiness: no vacío
es_telefono_valido = telefono.startswith("+") and len(telefono) == 13 and telefono[1:].isdigit()

# Verifica condiciones
if es_nombre_valido and es_telefono_valido:
    contactos.append((nombre, telefono))
    print("-------------")
    print("Contacto guardado")
else:
    print("-------------")
    print("Datos incorrectos")