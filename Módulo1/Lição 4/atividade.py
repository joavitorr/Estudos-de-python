notas = [45, 72, 88, 61, 90, 55, 78, 83, 40, 95]

# percorrendo a lista

for nota in notas:
    if nota >= 90:
        print(nota, "Excelente")
    elif nota >= 75 and nota <= 89:
        print(nota, "Bom")
    elif nota >= 60 and nota <= 74:
        print(nota, "regular")
    else:
        print(nota, "Reprovado")

# calculando as médias
indie = 0
total = 0
while indie < len(notas):
    total += notas[indie]
    indie += 1

media_geral = total / len(notas)    
print("Total de notas:", media_geral)

# Quantidades de alunos reprovados

total_reprovados = 0
for nota in notas:
    if nota < 60:
        total_reprovados += 1

print("Total de alunos reprovados:", total_reprovados)

# imprimindo a primeira nota acima de 85 e depois parar

for maior_nota in notas:
    if maior_nota >= 85:
        print(maior_nota)
        break