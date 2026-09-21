
#começa especificando os valores das variáveis
nome = 'João'
idade = 20
ano_experiencia = 1
salario = 870.80
empregado = False
especialidade = None

#Printa na tela as variáveis
print('Nome: ' + nome)
print('Idade: ' , idade)
print('Experiencia: ' , ano_experiencia)
print('Salario: ' , salario)
print('Empregado: ' , empregado)
print('Especialidade: ' , especialidade)

#Printa na tela os tipos de variáveis
print('Tipo de nome: ', type(nome))
print('Tipo de idade: ', type(idade))
print('Tipo de experiência: ', type(ano_experiencia))
print('Tipo de salario: ', type(salario))
print('Tipo empregado: ', type(empregado))
print('Tipo de especialidade: ', type(especialidade))

#faz a troca de int para float
idade = float(idade)
print(idade)