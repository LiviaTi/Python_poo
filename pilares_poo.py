# Herança 

print("\n Exemplo de herança")

#Classe Mãe
class Animal:
	def __init__(self, nome) -> None:
		self.nome = nome
	
	def andar(self):
		print(f"O animal {self.nome} andou")
		return

	def emitir_som(self):
		pass

#Classe Filha
class Cachorro(Animal):
	def emitir_som(self):
		return ("Au au")

#Classe Filha
class Gato(Animal):
	def emitir_som(self):
		return ("Miauu")

#Polimorfismo vai permitir utilizar o mesmo método já definido pela clase Mãe
#Implementado de uma nova forma. Mesmo nome com implemantação diferente
# Exemplo Acima = classe filha Cachorro e gato

dog = Cachorro(nome="Rex")
cat = Gato(nome="Thanos")

print("Exemplo de polimorfismo:")
animais = [dog, cat]
for animal in animais:
	print(f"{animal.nome} faz: {animal.emitir_som()}")
