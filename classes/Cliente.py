from .Pessoa import Pessoa
from .Conta import *

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta