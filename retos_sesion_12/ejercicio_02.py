#Tienes una app para gestionar tareas de 4 usuarios, para acceder los usuarios deben iniciar sesión con un nombre de usuario y una contraseña introducidos por teclado.
 
# Diccionario de usuarios y contraseñas
usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

# Solicita usuario y contraseña
usuario = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")

# Verifica el acceso
if usuario in usuarios and usuarios[usuario] == contraseña:
    print("Acceso Aprobado")
else:
    print("Acceso Denegado")