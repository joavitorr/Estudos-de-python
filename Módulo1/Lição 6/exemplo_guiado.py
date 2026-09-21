# EXEMPLO GUIADO

# Recebe dados do usuário
nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

# Processa os dados 
nome_formatado = nome.strip().title()
classificacao = "Aprovado" if nota >= 60 else "Reprovado"

# Exibe resultado com f-string
print(f"\nAluno: {nome_formatado}")
print(f"Nota: {nota:.2f}")
print(f"Situação: {classificacao}")
print(f"Tem {len(nome_formatado)} caracteres no nome")