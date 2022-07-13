from PySimpleGUI import PySimpleGUI as sg
import os
cwd = os.getcwd()
sg.theme('DarkRed')

# class Janela(sg):
# 	def login(self):
# 		self.Text()

# 		return self.Window()

def janela_login():

	layout = [
	[sg.Text('User'),sg.Input(key='user',size= (20,1))],
	[sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
	[sg.Button('Entrar',font='Verdana 14 italic bold underline')]
	]


	return sg.Window('Login',layout=layout,finalize=True,font='Verdana 14 italic bold')


def janela_tabela():

	layout = [
	[sg.Image(filename="grupos2.png",size=(1280,720))],
	[sg.Button('Grupo A',key='1',size=(11,3)),sg.Button('Grupo B',key='2',size=(11,3)),sg.Button('Grupo C',key='3',size=(11,3)),
	sg.Button('Grupo D',key='4',size=(11,3)),
	sg.Button('Grupo E',key='5',size=(11,3)),sg.Button('Grupo F',key='6',size=(11,3)),sg.Button('Grupo G',key='7',size=(11,3)),sg.Button('Grupo H',key='8',size=(11,3))],
	[sg.Button('Voltar',font='Verdana 12 italic bold underline')]

	]

	return sg.Window('Tabela',layout = layout,element_justification='c',font='Verdana 12 italic bold',finalize = True)

def janela_jogo(grupo):
	cwd = os.getcwd()

	image = cwd + '/bandeiras/grupo'

	vals = [['1','2','3','4'],['1','3','4','2'],['2','3','4','2']]
	aposta = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12']]
	tab = [0,0,0]


	for i in range(3):

		tab[i] = [

			[sg.Button('',button_color = sg.TRANSPARENT_BUTTON,
			image_filename = image + grupo + '/' + 'sel' + vals[i][0] + '.png' , image_size=(50,33), image_subsample=2, border_width=1,key='time'),
			sg.Input(key='aposta' + aposta[i][0],size= (2,1)),
			sg.Input(key='aposta'+ aposta[i][1],size= (2,1)),
			sg.ReadFormButton('',button_color = sg.TRANSPARENT_BUTTON,
			image_filename = image + grupo + '/' + 'sel' + vals[i][1] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time'),sg.Button('Estádio',key='estadio1')],
			[sg.Button('',button_color = sg.TRANSPARENT_BUTTON,
			image_filename = image + grupo + '/' + 'sel' + vals[i][2] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time'),
			sg.Input(key='aposta'+ aposta[i][2],size= (2,1)),
			sg.Input(key='aposta'+ aposta[i][3],size= (2,1)),
			sg.ReadFormButton('',button_color = sg.TRANSPARENT_BUTTON,
			image_filename = image + grupo + '/' + 'sel' + vals[i][3] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time'),sg.Button('Estádio',key='estadio2')]	
		]


	layout = [

		[sg.TabGroup([[
			sg.Tab('Primeira rodada',tab[0]),
			sg.Tab('Segunda Rodada',tab[1]),
			sg.Tab('Terceira Rodada',tab[2])]])],
			[sg.Button('Voltar',key='voltar3'),sg.Button('Apostar',key='apostar')]

	]



	return sg.Window('Jogos do Grupo ' + grupo ,layout = layout,finalize = True)


def janela_time():


	layout = [

		[sg.Image(filename='fotos_selecoes/fot25.png')],
		[sg.Text('O Brasil garantiu a sua vaga na Copa do Mundo de 2022 em 11 de novembro de 2021, mais de um ano antes do início do Mundial.\n'+
		'Com campanha praticamente perfeita nas Eliminatórias Sul-Americanas, a equipe de Tite pode até não ter encantado em muitos momentos,\n'+ 
		'mas sobrou na América do Sul com uma defesa aparentemente intransponível, um sistema de jogo sólido e Neymar chamando a responsabilidade no ataque.\n'+
		'O Brasil está no grupo G com Suíça, Sérvia e Camarões.')],
		[sg.Button('Voltar',key='voltar4')]
	]

	return sg.Window('Seleção',layout = layout,finalize = True)


janela1, janela2,janela3,janela4,janela5 = janela_login(),None,None,None,None

grupo = '1'

#stadium = [1,3,]

while True:

	window,event,values = sg.read_all_windows()
	print(event)

	if window == janela1 and event == sg.WIN_CLOSED:
		break

	if window == janela2 and event == sg.WIN_CLOSED or event == 'Voltar':
		janela2.hide()
		janela1.un_hide()

	if window == janela3 and event == sg.WIN_CLOSED or event == 'voltar3':
		janela3.hide()
		janela2.un_hide()

	if window == janela4 and event == sg.WIN_CLOSED or event == 'voltar4':
		janela4.hide()
		janela3.un_hide()

	if window == janela1 and event == 'Entrar':
		janela1.hide()
		janela2 = janela_tabela()
		

	if window == janela2 and event != 'Voltar': 
			janela2.hide()
			if not event:
				continue
			grupo = event
			janela3 = janela_jogo(grupo)

	if window == janela3 and event == 'apostar' or event == 'time':

		if event == 'apostar':
			print("aposta realizada")

			jogo = int(grupo) - 1
			avanco = jogo*6

			print(f"O jogo {avanco} vai ser {values['aposta1']} x {values['aposta2']}")
			print(f"O jogo {1 + avanco} vai ser {values['aposta3']} x {values['aposta4']}")
			print(f"O jogo {2 + avanco} vai ser {values['aposta5']} x {values['aposta6']}")
			print(f"O jogo {3 + avanco} vai ser {values['aposta7']} x {values['aposta8']}")
			print(f"O jogo {4 + avanco} vai ser {values['aposta9']} x {values['aposta10']}")
			print(f"O jogo {5 + avanco} vai ser {values['aposta11']} x {values['aposta12']}")

		if event == 'time':
			janela3.hide()
			janela4 = janela_time()
