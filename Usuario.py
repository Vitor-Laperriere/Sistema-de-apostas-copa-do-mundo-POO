# Classe que guarda informacoes sobre o usuario que ira acessar o sistema
class Usuario:

	# Construtor da classe
	def __init__(self, Nome = None, Senha = None, Saldo = 0, Indentificador = -1):

		self.nome = Nome
		self.senha = Senha
		self.saldo = Saldo
		self.ind = Indentificador

	def acessar_nome(self):
		return self.nome

	def acessar_saldo(self):
		return self.saldo

	def acessar_ind(self):
		return self.ind

	def adicionar_saldo(self, s):
		self.saldo += s

	def reduzir_saldo(self, s):
		self.saldo -= s