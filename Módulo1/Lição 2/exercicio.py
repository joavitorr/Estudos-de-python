
#Declarando variáveis
total_vendas = 85000
num_vendedores = 5
meta_mensal = 18000
maior_venda = 24000
menor_venda = 9500
tem_comissao = True

# Abaixo estão todos os cálculos proposto
media_vendas = total_vendas / num_vendedores
print("A média de vendas por vendedor foi de: ", media_vendas)

diferenca_venda = maior_venda - menor_venda
print('A diferença entre o valor mais alto e o mais baixo é de: ', diferenca_venda)


meta_media = media_vendas >= meta_mensal
print('Batemos a meta? ', meta_media)


resultado_comissao = tem_comissao and meta_media
print('Teremos comissão? ', resultado_comissao)


meta_mensal *= 2
print('O dobro da meta é: ', meta_mensal)


resto_divi = total_vendas % num_vendedores
print('O resto da divisão foi de: ', resto_divi)