
# Classiificando um vendedor com base na sua performance
vendas = 22000
meta = 18000
tem_comissao = True

# Verificamos se bateu a meta
if vendas >= meta:
    diferenca = vendas - meta
    print("Meta batida! Excedeu em:", diferenca)
elif vendas >= meta * 0.8: # atingiu pelo menos 80% da meta
    print("Quase lá - ficou abaixo da meta, mas dentro do aceitável")
else:
    print("Abaixo do aceitável - meta não atingida")

# Verifica elegibilidade para comissão
if tem_comissao and vendas >= meta:
    print("Elegível para comissão")
else:
    print("Sem comisssão nesse mês")
