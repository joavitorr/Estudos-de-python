
notas = [45, 72, 88, 61, 90, 55, 78, 83, 40, 95]

# percorrendo a lista

def classificar_nota(nota):
    if nota >= 90:
        return "Excelente"
    elif nota >= 75:
        return "Bom"
    elif nota >= 60:
        return "regular"
    else:
        return "Reprovado"

# calculando as médias
def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)

print("Média da turma:", calcular_media(notas))
# Quantidades de alunos reprovados

def qtd_reprovados(notas):
    total_reprovados = 0
    for nota in notas:
        if nota < 60:
            total_reprovados += 1
    return total_reprovados  # aqui

print("Quantidade de alunos reprovados:", qtd_reprovados(notas))

# imprimindo a primeira nota acima de 85 e depois parar
def limite_acima(notas, limite = 85):
    for nota in notas:
        if nota > limite:
            return nota
    return None
print("Maior nota acima da média:", limite_acima(notas))

for nota in notas:
    classificao = classificar_nota(nota)
    print(nota, "-", classificao)