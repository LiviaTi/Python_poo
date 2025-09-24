# Classe exemplo
class Pessoa:
	def __init__(self, nome, idade) -> None:
		self.nome = nome
		self.idade = idade
	def saudacao(self):
		return (f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos.")
#Objetos
pessoa1 = Pessoa("Livia", 24)
pessoa2 = Pessoa("Davi", 24)

mensagem = pessoa1.saudacao()

print(pessoa1.nome, pessoa2.nome)
print(mensagem)