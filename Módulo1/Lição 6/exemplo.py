nome = "joão silva"

len(nome)           # 10 — tamanho da string
nome.upper()        # "JOÃO SILVA" — tudo maiúsculo
nome.lower()        # "joão silva" — tudo minúsculo
nome.capitalize()   # "João silva" — só primeira letra maiúscula
nome.title()        # "João Silva" — primeira letra de cada palavra
nome.strip()        # remove espaços no início e no fim
nome.replace("joão", "carlos")  # "carlos silva"
nome.split(" ")     # ["joão", "silva"] — divide em lista

# VERIFICAÇÕES

nome.startswith("joão")  # True
nome.endswith("silva")   # True
"silva" in nome          # True — verifica se contém

# FORMATAÇÕES DE STRING

nome = "Ana"
idade = 28
print(f"Nome: {nome}, Idade: {idade}")  # Nome: Ana, Idade: 28

nota = 87,5
print(f"Nota: {nota:.2f}")

# RECEBENDO DADOS

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Precisamos especificar o tipo de variavel conforme desejamos, o input sempre retorna String

idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))
