#curso "o que é ciência da computação" USP/Coursera
#segunda Semana - entrada de dados (python)

segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

#pegar o valor inteiro da divisão
horas = total_segs // 3600
#pegar o resto da divisão
segs_restantes = total_segs % 3600
#pegar o valor inteiro da divisão
minutos = segs_restantes // 60
#pegar o resto da divisão
segs_restantes_final = segs_restantes % 60

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")
