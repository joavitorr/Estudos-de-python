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

    candidato = {"nome": nome_candi.strip().title(),
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

# ==========================
# MÉDIA GERAL DO CANDIDATOS
# ==========================

def media_candidatos(candidatos):
    total = 0
    for candidato in candidatos:
        total += candidato['nota']
    media = total / len(candidatos)

    return media

# ==========================
# MAIOR NOTA GERAL
# ==========================

def maior_nota_candidato(candidatos):
    maior_nota = candidatos[0]
    for candidato in candidatos:
        if candidato['nota'] > maior_nota['nota']:
            maior_nota = candidato

    return maior_nota

# =============================
# MENOR NOTA CANDIDATO
# ==========================

def menor_nota_candidato(candidatos):
    menor_nota = candidatos[0]
    for candidato in candidatos:
        if candidato['nota'] < menor_nota['nota']:
            menor_nota = candidato

    return menor_nota

# =============================
# CONTAR RECOMENDADOS
# ==========================

def contar_recomendados(candidatos):
    candidatos_recomendados = 0
    for candidato in candidatos:
        if candidato['nota'] >= 60 and candidato['experiencia'] >= 1 and len(candidato['nome']) > 5:
            candidatos_recomendados += 1

    return candidatos_recomendados    

# ==================
# BUSCADOR POR NOME
# ==================

def buscador_candidato(candidatos):
    nome_candidato = input("Digite o nome do candidato que você deseja bucar: ")

    for candidato in candidatos:
        if candidato['nome'].lower() == nome_candidato.lower():
            return candidato
    
    
    print("Candidato não encontrado")
    return None

        
# ===============
# BLOCO PRINCIPAL
# ===============

resultado = classificar_candidatos(candidatos)

for recomendado in resultado:
    print(f"{recomendado['nome']}: {recomendado['classificação']}")


media = media_candidatos(candidatos)
print(f"\nMédia de notas: {media:,.1f}")


maior_nota = maior_nota_candidato(candidatos)
print(f"\nO candidato: {maior_nota['nome']} tirou a maior {maior_nota['nota']} nota")

menor_nota = menor_nota_candidato(candidatos)
print(f"\nO candidato: {menor_nota['nome']} tirou a menor {menor_nota['nota']} nota")


recomendado = contar_recomendados(candidatos)
print(f"\nTotal de candidatos recomendados: {recomendado}")

candidato = buscador_candidato(candidatos)
if candidato is not None:
    print(f"\nCandidato: {candidato['nome']}, idade: {candidato['idade']}, experiência: {candidato['experiencia']}, nota: {candidato['nota']}")