class SaldoInsuficienteError(Exception):
    pass

class LimiteExcedidoError(Exception):
    pass

class Conta:
    def __init__(self, agencia: str, numero: int, saldo: float, limite: float):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        try:
            if valor > self.saldo:
                raise SaldoInsuficienteError("Saldo insuficiente para a operação.")
            if valor > self.limite:
                raise LimiteExcedidoError("O valor excede o limite permitido.")
            self.saldo -= valor
        except (SaldoInsuficienteError, LimiteExcedidoError) as e:
            print(f"Erro ao sacar: {e}")

class ContaCorrente(Conta):
    def __init__(self, agencia: str, numero: int, saldo: float):
        super().__init__(agencia, numero, saldo, limite=5000.00)

class ContaPoupanca(Conta):
    def __init__(self, agencia: str, numero: int, saldo: float):
        super().__init__(agencia, numero, saldo, limite=1000.00)