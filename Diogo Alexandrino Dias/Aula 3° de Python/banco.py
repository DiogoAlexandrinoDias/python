class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def get_saldo(self):
        return self.saldo


contaArthur = ContaBancaria(1000)

contaArthur.sacar(700)
contaArthur.depositar(1200)

print(contaArthur.get_saldo())