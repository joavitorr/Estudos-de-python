nome = "Ana"
anos_experiencia = 2
conhece_python = True
conhece_sql = False
nota_teste = 72

# Faz a verificação de anos de experiência
if anos_experiencia < 1:
    print("Sem experiência")
elif anos_experiencia <= 3:
    print("Junior")
else:
    print("Senior")

# Confere se possui conhecimento técnico
if conhece_python and conhece_sql:
    print("Perfil técnico completo")
elif conhece_python or conhece_sql:
    print("Perfil técnico parcial")
else:
    print("Sem habilidades técnicas")

# Confere a nota de teste
if nota_teste >= 80:
    print("Aprovado")
elif nota_teste >= 60 and nota_teste <= 79:
    print("Aprovado com ressalvas")
else:
    print("Reprovado")

# Resultado final
if nota_teste >= 60 and anos_experiencia >= 1 and conhece_python:
    print(nome, "Candidato recomendado")
else:
    print(nome, "Candidato não recomendado")