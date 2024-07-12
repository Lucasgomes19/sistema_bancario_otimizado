class Conta:
    def __init__(self, numero, titular, senha, saldo=0):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor, senha):
        if valor > 0 and self.saldo >= valor and self.senha == senha:
            self.saldo -= valor
            return True
        return False

    def consultar_saldo(self, senha):
        if self.senha == senha:
            return self.saldo
        return "Senha incorreta"


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular, senha):
        if numero not in self.contas:
            self.contas[numero] = Conta(numero, titular, senha)
            return True
        return False

    def depositar(self, numero, valor):
        if numero in self.contas:
            return self.contas[numero].depositar(valor)
        return False

    def sacar(self, numero, valor, senha):
        if numero in self.contas:
            return self.contas[numero].sacar(valor, senha)
        return False

    def consultar_saldo(self, numero, senha):
        if numero in self.contas:
            return self.contas[numero].consultar_saldo(senha)
        return "Conta não encontrada"


def depositar_em_conta(banco, numero_conta, valor):
    if banco.depositar(numero_conta, valor):
        print(f"Depósito de R${valor} realizado com sucesso na conta {numero_conta}")
    else:
        print(f"Falha ao realizar depósito na conta {numero_conta}")


def sacar_de_conta(banco, numero_conta, valor, senha):
    if banco.sacar(numero_conta, valor, senha):
        print(f"Saque de R${valor} realizado com sucesso na conta {numero_conta}")
    else:
        print(f"Falha ao realizar saque na conta {numero_conta} - senha incorreta ou saldo insuficiente")


def consultar_saldo_conta(banco, numero_conta, senha):
    saldo = banco.consultar_saldo(numero_conta, senha)
    if isinstance(saldo, str):
        print(f"Erro ao consultar saldo da conta {numero_conta}: {saldo}")
    else:
        print(f"Saldo da conta {numero_conta}: R${saldo}")


def main():
    meu_banco = Banco()
    meu_banco.criar_conta(12345, "Lucas", "senha123")

    depositar_em_conta(meu_banco, 12345, 500)
    consultar_saldo_conta(meu_banco, 12345, "senha123")

    sacar_de_conta(meu_banco, 12345, 200, "senha123")
    consultar_saldo_conta(meu_banco, 12345, "senha123")

    sacar_de_conta(meu_banco, 12345, 100, "senha_errada")

if __name__ == "__main__":
    main()
