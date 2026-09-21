#Python tem basicamente os mesmos operadores do Java, apenas com algumas alterações

10 // 3 #divisão inteira
10 ** 3 #potenciação

#Os operadores de comparação são os mesmos que o Java

10 == 3 #igual
10 != 3 #diferente
10 > 3  #maior que
10 < 3 #menor que
10 <= 3 #menor ou igual
10 >= 3 #maior ou igual

#Agora os operadores lógicos tem uma grande diferença. Diferente do Java que usa "||, && e !". O python nós escrevemos os operadores "And, Or e not"

True and False #Retorna false
True or False #Retorna true
not True #Retorna false

# ================== Exemplo guiado ==================

salario = 5000.0
bonus = 1200.0
imposto = 0.15 #15%

salario_bruto = salario + bonus
desconto = salario_bruto * imposto
salario_liquido = salario_bruto - desconto

print('Salario bruto: ', salario_bruto)
print('Desconto: ', desconto)
print('Salario liquido: ', salario_liquido)

# Comparação
meta = 5000.0
print('Bateu a meta?', salario_liquido >= meta)

# Lógica combinada
tem_bonus = True
acima_da_meta = salario_liquido > meta
print('Merece aumento? ', tem_bonus and acima_da_meta)

# Atribuição composto
salario_liquido += 300
print('Após reajuste: ', salario_liquido)