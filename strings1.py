mes = """janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro dezembro""".split()

d,m,a = input("dd/mm/aaaa: ").split("/")

print(f'{d} de {mes[int(m)-1]} {a}')
