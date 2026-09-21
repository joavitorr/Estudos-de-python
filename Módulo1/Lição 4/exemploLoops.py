
#Exemplo guiado
# Lista de vendas mensais de um vendedor

vendas = [12000, 19000, 8500, 22000, 15000]
meta = 18000

for venda in vendas:
    if venda >= meta:
        print(vendas, "- Meta batida")
    else:
        print(venda, "- Abaixo da meta")


# Calculando o total com while
total = 0
indice = 0
while indice < len(vendas):
    total += vendas[indice]
    indice += 1

print("Total de vendas:", total)

# Parando ao encontrar a primeira venda acima de 20000
print("Primeira venda acima de 20000:")
for venda in vendas:
    if venda > 20000:
        print(venda)
        break
