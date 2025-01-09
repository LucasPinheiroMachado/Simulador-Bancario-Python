from classes.Cliente import Cliente
from classes.Conta import ContaCorrente, ContaPoupanca
from classes.Banco import Banco

conta_corrente1 = ContaCorrente("001", 12345, 2000.0)
conta_poupanca1 = ContaPoupanca("001", 54321, 3000.0)
conta_corrente2 = ContaCorrente("002", 67890, 1000.0)

cliente1 = Cliente("João", 30, conta_corrente1)
cliente2 = Cliente("Maria", 25, conta_poupanca1)
cliente3 = Cliente("Carlos", 40, conta_corrente2)

banco = Banco(contas=[conta_corrente1, conta_poupanca1, conta_corrente2], 
              clientes=[cliente1, cliente2, cliente3])

# Testando depósito
print(f"Saldo inicial de João: {cliente1.conta.saldo}")
cliente1.conta.depositar(500.0)
print(f"Saldo após depósito: {cliente1.conta.saldo}")

# Testando saque com saldo suficiente
print("\nTentativa de saque de Maria:")
cliente2.conta.sacar(1000.0)
print(f"Saldo após saque: {cliente2.conta.saldo}")

# Testando saque com saldo insuficiente
print("\nTentativa de saque com saldo insuficiente por João:")
cliente1.conta.sacar(10000.0)

# Testando saque que excede o limite
print("\nTentativa de saque que excede o limite por Carlos:")
cliente3.conta.sacar(6000.0)

# Testando autenticação bem-sucedida
print("\nAutenticando João no banco com conta corrente:")
banco.autenticar("001", cliente1, conta_corrente1)

# Testando autenticação com agência inválida
print("\nAutenticando João no banco com agência inválida:")
banco.autenticar("999", cliente1, conta_corrente1)

# Testando autenticação com cliente inválido
print("\nAutenticando cliente não registrado no banco:")
cliente_invalido = Cliente("Lucas", 35, None)
banco.autenticar("001", cliente_invalido, conta_corrente1)

# Testando autenticação com conta inválida
print("\nAutenticando João com conta inválida:")
conta_invalida = ContaCorrente("001", 11111, 0.0)
banco.autenticar("001", cliente1, conta_invalida)
