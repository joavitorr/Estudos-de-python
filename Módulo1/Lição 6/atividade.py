nome = input("Seu nome completo: ")
idade = int(input("Sua idade: "))
anos_experiencia = int(input("Anos de experiência: "))
nota_teste = float(input("Nota do teste: "))

def classificao_teste(nota_teste):
    if nota_teste >= 90:
        return "Excelente"
    elif nota_teste >= 75:
        return "Bom"
    elif nota_teste >= 60:
        return "Regular"
    else:
        return "Reprovado"

def recomendacao(nota_teste, anos_experiencia, nome):
    if nota_teste >= 60 and anos_experiencia >= 1 and len(nome) > 5:
        return "Recomendado"
    else:
        return "Não recomendado"


def relatorio(nome, idade, anos_experiencia, nota_teste):
    nome_formatado = nome.strip().title()
    classificao = classificao_teste(nota_teste)
    recomendacao_candidato = recomendacao(nota_teste, anos_experiencia, nome)

    print(f"\nNome: {nome_formatado}")
    print(f"Idade: {idade}")
    print(f"Anos de Experiência: {anos_experiencia}")
    print(f"Nota: {nota_teste:.2f}")
    print(f"Sua classificação: {classificao}")
    print(f"Candidato: {recomendacao_candidato}")
    

relatorio(nome, idade, anos_experiencia, nota_teste)