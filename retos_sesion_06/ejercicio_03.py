#Imprime una tabla de verdad para la siguiente sentencia: "Un sistema de seguridad controla el acceso a una habitación, la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, pero no ambas al mismo tiempo. Si se introduce la tarjeta y la huella dactilar, la puerta no se abre. ¿Qué operador lógico se puede utilizar?
def puerta_se_abre(tarjeta, huella):
    # La puerta se abre si solo una de las dos opciones es True
    return tarjeta ^ huella  # XOR lógico

valores = [True, False]

print("Tarjeta\tHuella\t¿Puerta se abre?")
for tarjeta in valores:
    for huella in valores:
        estado = puerta_se_abre(tarjeta, huella)
        print(f"{tarjeta}\t{huella}\t{estado}")