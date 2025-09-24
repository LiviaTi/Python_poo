

print("\n Exemplo de encapsulamento:")
class ContaBancaria:
	def __init__(self, saldo) -> None:
		self.__saldo = saldo

	def depositar(self, valor):
		if valor > 0:
			self.__saldo += valor
	
	def sacar(self, valor):
		if valor > 0 and valor <= self.__saldo:
			self.__saldo -= valor
	
	def consultar_saldo(self):
		return self.__saldo

conta = ContaBancaria(saldo = 1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

#Abstração é um molde para criar outras classes
# não tem como instanciar



print("\n Exemplo de abstração")
from abc import ABC, abstractmethod

# Respeitam o método
class Veiculo(ABC):

	@abstractmethod
	def ligar(self):
		pass

	@abstractmethod
	def desligar(self):
		pass

class Carro(Veiculo):
	def __init__(self) -> None:
		pass
	
	def ligar(self):
		return ("Carro ligado")
	def desligar(self):
		return("Carro desligado")

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
