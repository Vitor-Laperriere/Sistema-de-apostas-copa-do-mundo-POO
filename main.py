from PySimpleGUI import PySimpleGUI as sg
import os
from fpdf import FPDF
#from Jogo import Jogo


cwd = os.getcwd()
sg.theme('DarkRed')

class Estadios:

	# 974 			0
	# albait 		1
	#aljanoub 		2
	#althumama 		3
	#binali 		4
	# education 	5
	#khalifa 		6
	# lusail 		7

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

	def acessar_arquivo_do_estadio(self, id_do_jogo):

		return self.arquivo_do_estadio[self.estadio_do_jogo[id_do_jogo]]

	def GUI(self, id_do_jogo):

		#id_do_estadio = self.estadio_do_jogo[num_do_jogo]
		#file = open('texto_estadios/' + 'estadio' + str(id_do_estadio) , 'r') #texto dos estadios devem estar em um arquivo do tipo estadio<i> com i de 0 a 7
		#read_text_from_file = file.read()

		layout = [
			[sg.Image('estadios/'+ self.acessar_arquivo_do_estadio(id_do_jogo))],
			#[sg.Text(read_text_from_file)]
			[sg.Button('Voltar',key='voltar5')]
		]

		return sg.Window('Estádio' + self.acessar_arquivo_do_estadio(id_do_jogo) ,layout = layout,finalize = True)


class Janela:

	def janela_login(self):

		layout = [
		[sg.Text('Usuário'),sg.Input(key='user',size= (20,1))],
		[sg.Text('Senha  '),sg.Input(key='senha',password_char='*',size=(20,1))],
		[sg.Button('Entrar',font='Verdana 14 italic bold underline')]
		]

		return sg.Window('Login',layout=layout,finalize=True,font='Verdana 14 italic bold', element_justification='c')

	def janela_tabela(self):

		layout = [
		[sg.Image(filename="grupos2.png",size=(1280,620))],
		[sg.Button('Grupo A',key='1',size=(11,3)),sg.Button('Grupo B',key='2',size=(11,3)),sg.Button('Grupo C',key='3',size=(11,3)),
		sg.Button('Grupo D',key='4',size=(11,3)),
		sg.Button('Grupo E',key='5',size=(11,3)),sg.Button('Grupo F',key='6',size=(11,3)),sg.Button('Grupo G',key='7',size=(11,3)),sg.Button('Grupo H',key='8',size=(11,3))],
		[sg.Button('Voltar',font='Verdana 12 italic bold underline',key='voltar2')]
		]

		return sg.Window('Tabela',layout = layout,element_justification='c',font='Verdana 12 italic bold',finalize = True)

	def janela_jogo(self,grupo):
		
		cwd = os.getcwd()
		image = cwd + '/bandeiras/grupo'

		vals = [['1','2','3','4'],['1','3','4','2'],['2','3','4','1']]
		aposta = [['0','0','1','1'],['2','2','3','3'],['4','4','5','5']]
		bets = [['0','1'],['2','3'],['4','5']]
		tab = [0,0,0]

		for i in range(3):

			tab[i] = [
				[sg.Button('',button_color = sg.TRANSPARENT_BUTTON,
				image_filename = image + grupo + '/' + 'sel' + vals[i][0] + '.png' , image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][0]),
				sg.Input(key='aposta0' + aposta[i][0],size= (2,1)),
				sg.Input(key='aposta1'+ aposta[i][1],size= (2,1)),
				sg.ReadFormButton('',button_color = sg.TRANSPARENT_BUTTON,
				image_filename = image + grupo + '/' + 'sel' + vals[i][1] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][1]),sg.Input(key='bet' + bets[i][0],size= (2,1)),
				sg.Button('Estádio',key='estadio1'+str(i))],
				[sg.Button('',button_color = sg.TRANSPARENT_BUTTON,
				image_filename = image + grupo + '/' + 'sel' + vals[i][2] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][2]),
				sg.Input(key='aposta0'+ aposta[i][2],size= (2,1)),
				sg.Input(key='aposta1'+ aposta[i][3],size= (2,1)),
				sg.ReadFormButton('',button_color = sg.TRANSPARENT_BUTTON,
				image_filename = image + grupo + '/' + 'sel' + vals[i][3] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][3]),sg.Input(key='bet' + bets[i][1],size= (2,1)),
				sg.Button('Estádio',key='estadio2'+str(i))]	
			]


		layout = [
			[sg.TabGroup([[
			sg.Tab('Primeira rodada',tab[0]),
			sg.Tab('Segunda Rodada',tab[1]),
			sg.Tab('Terceira Rodada',tab[2])]])],
			[sg.Button('Voltar',key='voltar3'),sg.Button('Apostar',key='apostar')]
		]

		return sg.Window('Jogos do Grupo ' + grupo ,layout = layout,finalize = True)


	def janela_estadio(self, id_do_jogo):

		self.estagio = Estadios()
		print("ID_DO_JOGO = ", id_do_jogo)
		return self.estagio.GUI(id_do_jogo);

	def janela_time(self,grupo,event):

		#mixer.init()

		#mixer.music.load('hinos/grupo' + grupo + '/' + 'hino' + event[4])  # cada grupo é um arquivo de 0 a 7 dentro os arquivos tem nome hino<i>.mp3 com i de 0 a 3

		file = open('texto_selecoes/grupo' + grupo + '/' + 'text' + event[4] + '.txt','r')

		read_text_from_file = file.read()

		layout = [

			[sg.Image(filename='fotos_selecoes/grupo' + grupo + '/' + 'fot' + event[4] + '.png'), # cada grupo é um arquivo de 0 a 7 dentro os arquivos tem nome fot<i>.mp3 com i de 0 a 3
			sg.Text(read_text_from_file)],
			[sg.Button('Voltar',key='voltar4')]
		]

		return sg.Window('Seleção',layout = layout,finalize = True)

	def escreve_recibo(self):

		# save FPDF() class into
		# a variable pdf
		pdf = FPDF()  
	  
		# Add a page
		pdf.add_page()
	  
		# set style and size of font
		# that you want in the pdf
		pdf.set_font("Arial", size = 15)


		vals = [[0,1,2,3],[0,2,3,1],[1,2,3,0]]

		file = open('selecoes.txt','r')

		num_do_jogo = int(0)
		for grupo in range (8):
			x = '-------------------- Grupo ' + str(grupo + 1) + '--------------------'
			pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
			linha = file.readline()
			selecoes = linha.split(',')
			for rodada in range(3):
				x = selecoes[vals[rodada][0]] + ' ' + str(game_bets[num_do_jogo][0]) + ' x ' + str(game_bets[num_do_jogo][1]) + ' ' + selecoes[vals[rodada][1]]
				pdf.cell(200, 10, txt = x, ln = 0, align = 'L')
				x = 'R$' + str(bet_price[num_do_jogo])
				pdf.cell(0, 10, txt = x, ln = 1, align = 'R') 

				num_do_jogo += 1
				x = selecoes[vals[rodada][2]] + ' ' + str(game_bets[num_do_jogo][0]) + ' x ' + str(game_bets[num_do_jogo][1]) + ' ' + selecoes[vals[rodada][3]]
				pdf.cell(200, 10, txt = x, ln = 0, align = 'L')
				x = 'R$ ' + str(bet_price[num_do_jogo])
				pdf.cell(0, 10, txt = x, ln = 1, align = 'R') 
				num_do_jogo += 1


		x = '----------------------------------------'
		pdf.cell(0, 10, txt = x, ln = 1, align = 'C') 

		x = nome_usuario
		pdf.cell(0, 10, txt = x, ln = 0, align = 'L')
		x = 'R$' + str(saldo_usuario)
		pdf.cell(0, 10, txt = x, ln = 0, align = 'R')


		pdf.output(nome_usuario + ".pdf")


		return


j = Janela()
janela = [None]*5
janela[0] = j.janela_login()

grupo = '1'
game_bets = [0]*48

for i in range(0,48):
	game_bets[i] = [-1,-1]

bet_price = [0]*48

nome_usuario = ' '
senha_usuario = ' '
saldo_usuario = 0

while True:

	window,event,values = sg.read_all_windows()
	print(event)

	if window and event == sg.WIN_CLOSED:
		break

	if window == janela[1] and event == 'voltar2':
		janela[1].hide()
		janela[0].un_hide()

	if window == janela[2] and event == 'voltar3':
		janela[2].hide()
		janela[1].un_hide()

	if window == janela[3] and event == 'voltar4':
		janela[3].hide()
		janela[2].un_hide()

	if window == janela[0] and event == 'Entrar':

		nome_usuario = values['user']
		senha_usuario = values['senha']
		janela[0].hide()
		janela[1] = j.janela_tabela()
		

	if window == janela[1] and event != 'voltar2':
		janela[1].hide()
		grupo = event
		janela[2] = j.janela_jogo(grupo)
		

	if window == janela[2] and event == 'apostar' or 'time' in event or 'estadio' in event:


		jogo = int(grupo) - 1
		num_do_jogo = int(jogo*6)

		if event == 'apostar':
			print("aposta realizada")

			for i in range(6):
				for j in range(2):
					if(values['aposta' + str(j) + str(i)] != ' ' and values['bet' + str(i)] != ' '):  # esse loop impede que insira apostas incompletas
						game_bets[num_do_jogo + i][j] = values['aposta' + str(j) + str(i)]			  
						bet_price[num_do_jogo + i] = values['bet' + str(i)]
					else:
						break


		if 'time' in event:

			janela[2].hide()
			janela[3] = j.janela_time(grupo,event)

		if 'estadio1' in event:
			if event[8] == '0':
				pass
			elif event[8] == '1':
				num_do_jogo = num_do_jogo + 2
			else: 
				num_do_jogo = num_do_jogo + 4	

			print(num_do_jogo)
			janela[2].hide()
			janela[4] = j.janela_estadio(num_do_jogo)

		if 'estadio2' in event:
			if event[8] == '0':
				num_do_jogo = num_do_jogo + 1
			elif event[8] == '1':
				num_do_jogo = num_do_jogo + 3
			else: 
				num_do_jogo = num_do_jogo + 5

			print(num_do_jogo)
			janela[2].hide()
			janela[4] = j.janela_estadio(num_do_jogo)


	if window == janela[4] and event == 'voltar5':
		janela[4].hide()
		janela[2].un_hide()



#j.escreve_recibo()