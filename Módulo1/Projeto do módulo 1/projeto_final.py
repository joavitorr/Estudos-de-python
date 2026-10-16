candidatos = []

qtd_candidatos = int(input("Digite a quantidade de candidatos que serão cadastrados: "))


while qtd_candidatos > 0:
    nome_candi = input("Digite o nome do candidato: ")
    idade_candi = int(input("Digite a idade do candidato: "))

    candidato = {"nome": nome_candi,
                  "idade": idade_candi}

    candidatos.append(candidato)

    qtd_candidatos -= 1

for candidato in candidatos:
        print("-------------------") 
        print(f"\nNome: {candidato['nome']}")
        print(f"Idade: {candidato['idade']}")
        print("-------------------")   