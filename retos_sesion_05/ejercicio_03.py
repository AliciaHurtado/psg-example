# Convierte segundos a semanas, días, horas, minutos y segundos
total_segundos = 1000000
semanas = total_segundos // (7*24*3600)
resto = total_segundos % (7*24*3600)
dias = resto // (24*3600)
resto %= (24*3600)
horas = resto // 3600
resto %= 3600
minutos = resto // 60
segundos = resto % 60

print(f"{total_segundos} segundos = {semanas} semanas {dias} días {horas} horas {minutos} minutos {segundos} segundos")