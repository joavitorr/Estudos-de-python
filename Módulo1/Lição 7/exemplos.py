# =================== LISTAS ==========================

notas = [7.5, 8.0, 6.5, 9.0]

notas[0] # 7.5 - Indice começa com 0
notas[-1] # 9.0 - Último elemento
notas[1:3] # [8.5, 6.5] - fatiamento - índice final não incluso

notas.append(10.0) # adiciona no fim
notas.remove(6.5) # remove o valor
notas.pop(0) # remove e retorna pelo índice
len(notas) # tamanho da lista
sorted(notas) # retorna nova lista ordenada
notas.sort() # ordena a própria lista

# =====================================================

# ================== DICIONÁRIO =======================

candidato = {
    "nome": "Ana",
    "idade": 28,
    "nota": 87.5,
    "aprovado": True
}

candidato["nome"] # "Ana" - Acessando pela chave
candidato["cidade"] = "SP" # Adicionando uma nova chave
candidato["idade"] = "29" # Atualizando um valor existente

candidato.keys() # todas as chaves
candidato.values() # todos os valores

"nome" in candidato # Verifica se a chave existe

# ================ ITERANDO ============================

for chave, valor in candidato.items():
    print(f"{chave}: {valor}")

# ======================================================

# ================ LISTA DE DICIONÁRIOS ===================

candidatos = [
    {"nome": "Ana", "nota": 87.5},
    {"nome": "Carlos", "nota": 54.0},
    {"nome": "Maria", "nota": 91.0},
]

for c in candidatos:
    print(c["nome"], c["nota"])