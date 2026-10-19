# ---------- definição da classe ----------
class ContaBancaria:
    # atributo de classe: compartilhado por todas as contas
    banco = "Banco Python"

    # construtor: roda automaticamente ao criar o objeto
    def  __init__(self, titular, saldo_inicial):
        # atributos de instância: cada objeto tem os seus
        self.titular = titular
        self.saldo = saldo_inicial

    # método: note o self como primeiro parâmetro
    def depositar(self, valor):
        # self.saldo acessa o atributo do objeto; valor é variável local
        self.saldo += valor

    def sacar(self, valor):
        # validação antes de alterar o estado do objeto

        if valor > self.saldo:
            print(f"Saldo insuficiente para {self.titular}.")
        else:
            self.saldo -= valor

    # equivalente ao toString() do Java
    def __str__(self):
         return f"{self.titular} - saldo: R$ {self.saldo:.2f}"
    

# ---------- USO --------------
# criar objetos chama o __init__; não passamos o self, o Pyhon passa
conta_ana = ContaBancaria("Ana", 1000)
conta_beto = ContaBancaria("Beto", 500)

conta_ana.depositar(250)
conta_beto.sacar(800) # vai cair no if do 'saque'

# cada objeto tem seu próprio estado
print(conta_ana) # usa o __str__
print(conta_beto)

# acesso direto a atributo (sem getter/setter, é padrão em Python)
print(f"Titular: {conta_ana.titular}")

# atributo de classe, acessível pelo objeto ou pela class
print(f"Banco: {ContaBancaria.banco}")
        
