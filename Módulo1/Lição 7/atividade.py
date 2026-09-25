candidatos = [
    {"nome": "Ana Lima",    "idade": 28, "experiencia": 3, "nota": 88.0},
    {"nome": "Carlos Mota", "idade": 22, "experiencia": 0, "nota": 55.0},
    {"nome": "Maria Silva", "idade": 35, "experiencia": 5, "nota": 92.0},
    {"nome": "Pedro Alves", "idade": 26, "experiencia": 1, "nota": 67.0},
    {"nome": "Julia Costa", "idade": 30, "experiencia": 2, "nota": 74.0}
]

# Percorrendo a lista e classificando candidatos

def classificar_candi(candidatos):
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
    classificacao = classificar_candi(c['nota'])
    print(f"{c['nome']}: classificacao: {classificacao}")