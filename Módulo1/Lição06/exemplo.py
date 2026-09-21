nome = "João Silva"

# Operações básicas com String

len(nome) #tamanho da string
nome.upper() #tudo maiúsculo
nome.lower() #tudo minúsculo
nome.capitalize() #só a primeira letra maiúscula
nome.title() #primeira letra de cada palavra maiúscula
nome.strip() #remove espaços no início e no fim
nome.replace("João", "Carlos") #Carlos Silva
nome.split(" ") # ["joão", "silva"] - divide em lista

# Verificações

nome.startswith("joão") # true
nome.endswith("silva") # true
"silva" in nome # verifica se contém

