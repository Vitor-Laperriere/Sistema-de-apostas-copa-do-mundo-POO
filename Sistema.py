import csv
import pandas as pd
from Usuario import Usuario

class Sistema:

	arquivo_usuarios = f'./admin.csv'

	def __init__(self):

		self.tabela = pd.read_csv(f'./admin.csv', sep=',')

	def login_valido(self, nome, senha):

		for i in self.tabela.index:
			if self.tabela['nome'][i] == nome and self.tabela['senha'][i] == senha:
				return True

		return False

	def registrar_usuario(self, usuario):

		f = open(f'./admin.csv', 'a', newline='\n')
		writer = csv.writer(f)
		linha = [str(usuario.ind), usuario.nome, usuario.senha, str(usuario.saldo)]
		writer.writerow(linha)
		f.close()

		self.tabela = pd.read_csv(f'./admin.csv', sep=',')

if __name__ == '__main__':

	s = Sistema()
	otavio = Usuario('Otavio', '12', 2, 1)

	s.registrar_usuario(otavio)

	if s.login_valido(otavio.nome, otavio.senha):
		print("Login :)")
	else:
		print("Sem Login :(")
