#Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.
print("Método intersection()")
print("Método difference()")

tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

# Convertimos las listas en conjuntos
conjunto_fisica = set(tienda_fisica)
conjunto_online = set(tienda_online)

# a. Compraron en ambos canales
ambos = conjunto_fisica & conjunto_online
print("a. Compraron en ambos:", ambos)

# b. Solo en tienda física
solo_fisica = conjunto_fisica - conjunto_online
print("b. Solo en tienda física:", solo_fisica)

# c. Solo online
solo_online = conjunto_online - conjunto_fisica
print("c. Solo online:", solo_online)