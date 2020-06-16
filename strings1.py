# O comando split() criará uma list de strings separadas com índice iniciado a partir de 0
mes = """janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro dezembro""".split()

# Permitirá a entrada do dia, mês e ano e tambem da /
d,m,a = input("dd/mm/aaaa: ").split("/")

#Converterá a entrada do mês em inteiro para o mês por extenso tirado da lista mes
print(f'{d} de {mes[int(m)-1]} {a}')

