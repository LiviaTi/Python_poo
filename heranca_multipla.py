class Animal():
	def __init__(self, nome) ->None:
		self.nome = nome
	
	def emitir_som(self):
		pass

class Mamifero(Animal):
	def amamentar(self):
		return (f"{self.nome} está amamentando.")

class Ave(Animal):
	def voar(self):
		return (f"{self.nome} está voando")
# no caso da classe mãe estar emitindo som usa super()
# super() é uma função padrão que chama a implementação da classe mãe e faz algo a mais
class Morcego(Mamifero, Ave):
	def emitir_som(self):
		#super().emitir_som():
		return ("Morcegos emitem sons ultrassônicos")

#Acessando métodos das classes bases 'Animal'
morcego = Morcego(nome="Batman")
print("Nome do morcego: ", morcego.nome)
print("Som do morcego: ",morcego.emitir_som())

#Acessando métodos da classe 'Mamífero' e 'Ave'
print("Morcego amamentando: ", morcego.amamentar())
print("Morcego voando: ", morcego.voar())


