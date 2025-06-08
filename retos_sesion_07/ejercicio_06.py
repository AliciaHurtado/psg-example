
texto = "   hola, bienvenidos a la sesión 07.   "

# 1. strip() - elimina espacios al inicio y final
print("1. strip():", texto.strip())

# 2. capitalize() - pone la primera letra en mayúscula
print("2. capitalize():", texto.strip().capitalize())

# 3. title() - pone en mayúscula la primera letra de cada palabra
print("3. title():", texto.strip().title())

# 4. swapcase() - invierte mayúsculas y minúsculas
print("4. swapcase():", texto.strip().swapcase())

# 5. startswith() - verifica si comienza con un substring
print("5. startswith('hola'):", texto.strip().startswith("hola"))