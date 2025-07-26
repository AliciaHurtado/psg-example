#Imprimir los 20 primeros números de la sucesión de Lucas.
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

for i in range(20):
    print(lucas(i), end=" ")