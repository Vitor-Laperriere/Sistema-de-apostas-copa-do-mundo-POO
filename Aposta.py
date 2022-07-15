class Aposta:

	#	Construtor da classe Aposta
	def __init__(self, TabelaDeApostas = None):

		if TabelaDeApostas == None:
			#	Iniciando a tabela de apostas com campos vazios (-1)			
			tabela = []
			for i in range(48):
				tabela.append([-1, -1, -1])
		
		else:

			tabela = TabelaDeApostas

	#	Funcao que adiciona uma aposta de um determinado jogo
	def adicionar_aposta_do_jogo(self, idJogo, golsTime1, golsTime2, dinheiroApostado):
		
		tabela[idJogo][0] = golsTime1
		tabela[idJogo][1] = golsTime2
		tabela[idJogo][2] = dinheiroApostado

	#	Funcao que remove uma aposta de um determinado jogo
	def remover_aposta_do_jogo(self, idJogo)

		tabela[idJogo][0] = -1
		tabela[idJogo][1] = -1
		tabela[idJogo][2] = -1

