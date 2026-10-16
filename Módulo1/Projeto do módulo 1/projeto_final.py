candidatos = []

qtd_candidatos = int(input("Digite a quantidade de candidatos que serão cadastrados: "))

# ====================
# CADASTRO DE USUÁRIOS
# ====================

while qtd_candidatos > 0:
    nome_candi = input("Digite o nome do candidato completo: ")
    idade_candi = int(input("Digite a idade do candidato: "))
    experiencia_candi = int(input("Digite quanto tempo de experiência o candidato tem: "))
    nota_candi = float(input("Qual a nota do candidato: "))

    candidato = {"nome": nome_candi,
                  "idade": idade_candi,
                  "experiencia": experiencia_candi,
                  "nota": nota_candi}

    candidatos.append(candidato)

    qtd_candidatos -= 1

# ==========================
# CLASSIFICAÇÃO DO CANDIDATO
# ==========================

def classificar_candidatos(candidatos):
    resultado = []
    for candidato in candidatos:
        nota = candidato['nota']

        if nota >= 90:
            classificacao = "Excelente"
        elif nota >= 75:
            classificacao = "Bom"
        elif nota >= 60:
            classificacao = "Regular"
        else:
            classificacao = "Reprovado"
        
        resultado.append({"nome": candidato['nome'],
                          "idade": candidato['idade'],
                          "experiencia": candidato['experiencia'],
                          "nota": candidato['nota'],
                          "classificação": classificacao})
            
    return resultado

resultado = classificar_candidatos(candidatos)

for recomendado in resultado:
    print(f"{recomendado['nome']}: {recomendado['classificação']}")
        