# @classmethod
# @staticmethod

#cls recebe a classe
#cls não consegue acessar os valores da instancia self
class MinhaClasse:
	valor = 10

	def __init__(self, nome) -> None:
		self.nome = nome
	
	def metodo_instancia(self):
		return (f"Método de instância (self), Ações do objeto, chamado para {self.nome}")
	
	@classmethod
	def metodo_classe(cls): #cls recebe a clase
		return (f"Método da classe chamado para valor = {cls.valor}. cls, Criar instâncias, acessar/alterar a classe")
	
	@staticmethod
	def metodo_estatico():
		return "Método estático: Funções utilitárias relacionadas à classe"

obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
	def __init__(self, marca, modelo, ano)-> None:
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
	
	@classmethod
	def criar_carro(cls, configuracao):
		marca, modelo, ano = configuracao.split(",")
		return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"\n Marca: {carro1.marca} \n Modelo: {carro1.modelo} \n Ano: {carro1.ano}\n ")

# @staticmethod é muito utilizado em bibliotecas

class	Matematica:
	@staticmethod
	def somar(a, b):
		return a + b

print(Matematica.somar(a=10, b=15))
