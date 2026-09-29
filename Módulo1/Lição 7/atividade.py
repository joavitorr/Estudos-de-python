candidatos = [
    {"nome": "Ana Lima",    "idade": 28, "experiencia": 3, "nota": 88.0},
    {"nome": "Carlos Mota", "idade": 22, "experiencia": 0, "nota": 55.0},
    {"nome": "Maria Silva", "idade": 35, "experiencia": 5, "nota": 92.0},
    {"nome": "Pedro Alves", "idade": 26, "experiencia": 1, "nota": 67.0},
    {"nome": "Julia Costa", "idade": 30, "experiencia": 2, "nota": 74.0}
]

# Percorrendo a lista e classificando candidatos

def classificar_candidatos(candidatos):
    if candidatos >= 90:
        return "Excelente"
    elif candidatos >= 75:
        return "Bom"
    elif candidatos >= 60:
        return "regular"
    else:
        return "Reprovado"
        
# Percorrendo a lista e imprimindo a média

total = 0
for m in candidatos:
    total += m["nota"]
media = total / len(candidatos)
print(f"\nMédia de notas: {media:,.1f}")


for c in candidatos:
    classificacao = classificar_candidatos(c['nota'])
    print(f"{c['nome']}: classificacao: {classificacao}")


#MAIOR NOTA
maior_nota = candidatos[0]
for nota in candidatos:
    if nota['nota'] > maior_nota['nota']:
        maior_nota = nota
print(f"Maior nota: {maior_nota['nome']} com {maior_nota['nota']:,.1f}")


#TOTAL DE CANDIDATOS COM INCLUSÃO
candidatos.append({"nome": "Lucas Rocha", "idade": 24, "experiencia": 1, "nota": 81.0})
print(f"\nTotal de candidatos: {len(candidatos)}")


# Candidatos recomendados
candidatos_recomendados = 0
for recom in candidatos:
    if recom['nota'] >= 60 and recom['experiencia'] >= 1 and len(recom['nome']) > 5:
        candidatos_recomendados += 1
print(f"\nTotal de candidatos recomendados: {candidatos_recomendados}")
