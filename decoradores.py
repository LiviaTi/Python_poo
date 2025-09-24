#decoradores é um tipo especial de função que permite modificar ou extender funções
#Sem alterar o código original

#Decoradores são muito utilizados para validação, exemplo em uma tividade de site precisa saber se o usuário está logado

#wrapper envolve a função
def meu_decorador(func):
	def wrapper():
		print("Antes da função ser chamada")
		func()
		print("Depois da função ser chamada")
	return wrapper

@meu_decorador
def minha_funcao():
	print("Minha função foi chamada")

minha_funcao()

from typing import Any
#Mesma coisa so que chamamos na estrutura de classe
class MeuDecoradorDeClasse:
	def __init__(self, func) -> None:
		self.func = func

	def __call__(self) -> Any:
		print("Antes da função ser chamada (Decorador de classe):")
		self.func()
		print("Depois da função ser chamada (Decorador de classe):")

@MeuDecoradorDeClasse
def segunda_funcao():
	print("Minha segunda função foi chamada")

segunda_funcao()