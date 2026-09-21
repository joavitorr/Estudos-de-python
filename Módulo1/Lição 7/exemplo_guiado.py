# Lista de dicionários representando vendedores
vendedores = [
    {"nome": "João", "vendas": 22000, "meta": 18000},
    {"nome": "Ana",  "vendas": 15000, "meta": 18000},
    {"nome": "Pedro","vendas": 19500, "meta": 18000}
]

# Percorrendo e classificanco cada vendedor
for v in vendedores:
    bateu = v["vendas"] >= v["meta"]
    status = "Bateu a meta" if bateu else "Abaixo da meta"
    print(f"{v['nome']}: R${v['vendas']:,.0f} - {status}")

# Calculando a média de vendas

total = 0
for v in vendedores:
    total += v["vendas"]
media = total / len(vendedores)
print(f"\nMédia de vendas: R${media:,.0f}")

# Encontrando o maior vendedor
maior = vendedores[0]
for v in vendedores:
    if v["vendas"] > maior["vendas"]:
        maior = v
print(f"Maior vendedor: {maior['nome']} com R${maior['vendas']:,.0f}")