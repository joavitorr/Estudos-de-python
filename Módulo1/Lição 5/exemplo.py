"""def somar(a, b):
    return a + b"""

def saudacao(nome, mensagem="Olá"):
    print(mensagem, nome)

saudacao("João")
saudacao("João", "Oi")

# retorno de valores

def calcular_media(total, quantidade):
    return total / quantidade

media = calcular_media(500, 5)
print(media)

# variáveis dentro da função só existem dentro dela

"""def minha_funcao():
    x = 10
    return x

print(x)"""

# exemplo guiado

# funcao que classifica o aluno com base na nota
def classificar_nota(nota):
    if nota >= 90:
        return "Excelente"
    elif nota >= 75:
        return "Bom"
    elif nota >= 60:
        return "Regular"
    else:
        return "Reprovado"

# Função que calcula a média de uma lista
def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)

# Usando as funções
notas = [45, 72, 88, 61, 90, 55, 78, 83, 40, 95]

for nota in notas:
    classificacao = classificar_nota(nota)
    print(nota, "-", classificacao)

media = calcular_media(notas)
print("Média da turma:", media)