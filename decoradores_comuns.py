# @classmethod
# @staticmethod

#cls recebe a classe
#cls não consegue acessar os valores da instancia self
class MinhaClasse:
	valor = 10

	def __init__(self, nome) -> None:
		self.nome = nome
	
	def metodo_instancia(self):
		return (f"Método de instância chamado para {self.valor}")
	
	@classmethod
	def metodo_classe(cls):
		return (f"Método da classe chamado para valor = {cls.valor}")


obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())

