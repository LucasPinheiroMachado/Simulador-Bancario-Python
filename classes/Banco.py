from .Cliente import Cliente
from .Conta import *

class Banco:
    def __init__(self, contas, clientes):
        if not all(isinstance(conta, Conta) for conta in contas):
            raise ValueError("Todos os elementos de 'contas' devem ser instâncias de Conta.")
        if not all(isinstance(cliente, Cliente) for cliente in clientes):
            raise ValueError("Todos os elementos de 'clientes' devem ser instâncias de Cliente.")
        
        self.contas = contas
        self.clientes = clientes

    def autenticar(self, agencia: str, cliente: Cliente, conta: Conta) -> bool:
        if not any(c.agencia == agencia for c in self.contas):
            print("Agência não pertence ao banco.")
            return False

        if cliente not in self.clientes:
            print("Cliente não pertence ao banco.")
            return False

        if conta not in self.contas:
            print("Conta não pertence ao banco.")
            return False

        if cliente.conta != conta:
            print("Conta não pertence ao cliente fornecido.")
            return False

        print("Autenticação bem-sucedida!")
        return True