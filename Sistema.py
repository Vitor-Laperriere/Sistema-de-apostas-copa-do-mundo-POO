import csv
import pandas as pd
from Usuario import Usuario

class Sistema:

	arquivo_usuarios = f'./users.csv'

	def __init__(self):

		self.tabela = pd.read_csv(self.arquivo_usuarios, sep=',')

	def usuario_registrado(self, usuario):

		for i in self.tabela.index:
			if self.tabela['nome'][i] == usuario.nome and\
				self.tabela['senha'][i] == usuario.senha and\
				 self.tabela['saldo'][i] == usuario.saldo and\
				  self.tabela['id'][i] == usuario.ind:
				return True

		return False

	def login_valido(self, nome, senha):

		for i in self.tabela.index:

			if str(self.tabela['nome'][i]) == nome and str(self.tabela['senha'][i]) == senha:
				return True

		return False

	def registrar_usuario(self, usuario):

		#	Caso onde usuario ja foi registrado
		if self.usuario_registrado(usuario):
			return

		f = open(self.arquivo_usuarios, 'a', newline='\n')
		writer = csv.writer(f)
		linha = [str(usuario.ind), usuario.nome, usuario.senha, str(usuario.saldo)]
		writer.writerow(linha)
		f.close()

		self.tabela = pd.read_csv(self.arquivo_usuarios, sep=',')

if __name__ == '__main__':

	s = Sistema()
	otavio = Usuario('Otavio', '12', 2, 1)

	s.registrar_usuario(otavio)

	if s.login_valido(otavio.nome, otavio.senha):
		print("Login :)")
	else:
		print("Sem Login :(")
