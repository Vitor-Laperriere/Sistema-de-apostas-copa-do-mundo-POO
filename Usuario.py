#	Classe que guarda informacoes sobre o usuario que ira acessar o sistema
class Usuario:

	def __init__(self, Nome = None, Senha = None, Saldo = 0, Indentificador = -1):

		nome = Nome
		senha = Senha
		saldo = Saldo
		ind = Indentificador

	def acessar_nome(self):
		return nome

	def acessar_saldo(self):
		return saldo

	def acessar_ind(self):
		return ind

	def adicionar_saldo(self, s):
		saldo += s

	def reduzir_saldo(self, s):
		saldo -= s

	def __str__(self):
		return f'Usuário {nome} possui saldo de R$ {saldo} na conta.'