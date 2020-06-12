nome = "reginaldo dos santos aquino"
print(nome)

# Converte para maiúscula a primeira letra de cada nome
print(nome.title())

# Imprime a quantidade de caracteres, incluindo os espaços em branco
print(len(nome))

# Remove espaços em branco no começo e no final da string
no_white_space = " reginaldo dos santos aquino ".strip()
print(len(no_white_space))

# Retorna a quantidade de palavras na string
name = len(nome.split())
print(name)

# Eliminando os espaços internos na contagem
qtd_espaco = 0
qtd_letras = ""
for n in nome:
    if(n == " "):
        qtd_espaco += 1
    qtd_letras += n
    
print("soma das letras sem espaços", len(qtd_letras)-qtd_espaco)

# Eliminando os espaços internos na contagem
soma_letras = 0
for n in nome.split():
    soma_letras += len(n)
print("soma das letras sem espaços", soma_letras)

# Eliminando os espaços internos na contagem, forma mais simples
print("soma das letras sem espaços", len(nome) - nome.count(" "))

# Conta a quantidade de vezes que a letra a ocorre na string
print(nome.count("a"))

# Retorna o indece onde a string passada no parâmetro inicia
print(nome.index("santos"))

# Retorna o indece onde a string passada no parâmetro inicia
print(nome.find("aquino"))
# Armazena na variável n os nove primeiros caracteres
n = nome[:9]
print(n)

# Armazena na variável o nome completo com todas as letras maiúsculas
nome_maiusculo = nome.upper()
print(nome_maiusculo)

# Armazena na variável o nome completo com todas as letras manúsculas
nome_minusculo = nome.lower()
print(nome_minusculo)



first_name = "Louise"
last_name = " Sousa"
# Concatenando strings
full_name = first_name + last_name
print(full_name)

# Usando formatação
print(f"{first_name}{last_name}")

print("{}{}".format(first_name, last_name))