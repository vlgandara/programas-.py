g = input("Por favor, entre com o número de segundos que deseja converter:")
segundosInteiro = int(g)

dia = segundosInteiro // 86400
segs_restantes = segundosInteiro % 86400
hora = segs_restantes // 3600
segs_restantes2 = segundosInteiro % 3600
minuto = segs_restantes2 // 60
segs_restantes3 = segundosInteiro % 60

print(dia, "dias,",hora,"horas,",minuto, "minutos e",segs_restantes3,"segundos.")
