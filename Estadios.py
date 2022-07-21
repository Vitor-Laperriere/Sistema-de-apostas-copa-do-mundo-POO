import PySimpleGUI as sg
	
# Classe que armazena as informacoes dos estadios
class Estadios:

	# 974 			0
	# albait 		1
	#aljanoub 		2
	#althumama 		3
	#binali 		4
	# education 	5
	#khalifa 		6
	# lusail 		7

	# Construtor da classe
	def __init__(self):
		
		self.arquivo_do_estadio = ['974.png','Al_Bayt_Stadium.png','aljanoub.png',
			'althumama.png','binali.png','education.png','khalifa.png', 'lusail.png']

		self.estadio_do_jogo = [
			1,3,3,6,6,1,	#	Grupo A
			6,4,4,1,4,3,	#	Grupo B
			0,7,5,7,0,7,	#	Grupo C
			2,5,2,0,2,5,	#	Grupo D
			3,6,4,1,6,1,	#	Grupo E
			4,1,3,6,4,3,	#	Grupo F
			7,2,2,0,0,7,	#	Grupo G
			5,0,5,7,2,5 	#	Grupo H
		]

	# Metodo que retorna o nome do arquivo da foto de um determinado estadio
	def acessar_arquivo_do_estadio(self, id_do_jogo):

		return self.arquivo_do_estadio[self.estadio_do_jogo[id_do_jogo]]

	# Metodo que retorna uma janela com as informacoes de um determinado estadio 
	def GUI(self, id_do_jogo):

		id_do_estadio = self.estadio_do_jogo[id_do_jogo]
		file = open('textos/estadios/' + str(id_do_estadio)+ '.txt' , 'r') #texto dos estadios devem estar em um arquivo do tipo estadio<i> com i de 0 a 7
		read_text_from_file = file.read()

		layout = [
			[sg.Image('./fotos/estadios/'+ self.acessar_arquivo_do_estadio(id_do_jogo))],
			[sg.Text(read_text_from_file, size = (60, None), font=("Helvetica", 12))],
			[sg.Button('Voltar',key='voltar5')]
		]

		return sg.Window('Estádio' + self.acessar_arquivo_do_estadio(id_do_jogo) ,layout = layout,finalize = True)
