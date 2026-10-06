candidatos = [
    {"nome": "Ana Lima",    "idade": 28, "experiencia": 3, "nota": 88.0},
    {"nome": "Carlos Mota", "idade": 22, "experiencia": 0, "nota": 55.0},
    {"nome": "Maria Silva", "idade": 35, "experiencia": 5, "nota": 92.0},
    {"nome": "Pedro Alves", "idade": 26, "experiencia": 1, "nota": 67.0},
    {"nome": "Julia Costa", "idade": 30, "experiencia": 2, "nota": 74.0}
]


# Percorrendo a lista e classificando candidatos

def classificar_candidatos(candidatos):
    for candidato in candidatos:
        nota = candidato['nota']

        if nota >= 90:
            classificacao = "Excelente"
        elif nota >= 75:
            classificacao = "Bom"
        elif nota >= 60:
            classificacao = "regular"
        else:
            classificacao = "Reprovado"
        
        print(f"{candidato['nome']}: classificação: {classificacao}")
        
# Candidatos recomendados
def contar_recomendados(candidatos):
    candidatos_recomendados = 0
    for candidato in candidatos:
        if candidato['nota'] >= 60 and candidato['experiencia'] >= 1 and len(candidato['nome']) > 5:
            candidatos_recomendados += 1
    print(f"\nTotal de candidatos recomendados: {candidatos_recomendados}")


# Percorrendo a lista e imprimindo a média

def media_candidatos(candidatos):
    total = 0
    for candidato in candidatos:
        total += candidato['nota']
    media = total/ len(candidatos)
    
    print(f"\nMédia de notas: {media:,.1f}")

    return media 

#MAIOR NOTA

def encontrar_maior_nota(candidatos):
    maior_nota = candidatos[0]
    for candidato in candidatos:
        if candidato['nota'] > maior_nota['nota']:
            maior_nota = candidato
    print(f"Maior nota: {maior_nota['nome']} com {maior_nota['nota']:,.1f}")


#Bloco principal
classificar_candidatos(candidatos)
media_candidatos(candidatos)
encontrar_maior_nota(candidatos)
contar_recomendados(candidatos)


#TOTAL DE CANDIDATOS COM INCLUSÃO
candidatos.append({"nome": "Lucas Rocha", "idade": 24, "experiencia": 1, "nota": 81.0})
print(f"\nTotal de candidatos: {len(candidatos)}")