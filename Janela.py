from PySimpleGUI import PySimpleGUI as sg
from pygame import mixer
from Selecao import Selecao
from Estadios import Estadios

# Classe responsavel por criar janelas na interface grafica
class Janela:

    # Metodo da janela de login
    def janela_login(self):

        layout = [
            [sg.Image(filename="./fotos/BETUSP.png", size=(1280, 720))],
            [sg.Text('Usuário'), sg.Input(key='user', size=(20, 1))],
            [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
            [sg.Button('Registrar', font='Verdana 14 italic bold underline'),
             sg.Button('Entrar', font='Verdana 14 italic bold underline')],
            [sg.Text('',key='aviso_registro',font='Verdana 10')]
        ]

        return sg.Window('Login', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    # Metodo da janela de aviso de usuario ja registrado
    def janela_usuario_ja_registrado(self):

        layout = [
            [sg.Text('Nome de usuário já registrado.')],
            [sg.Text('Tente outro.')],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltarDoAviso')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    # Metodo da janela de aviso de usuario nao registrado
    def janela_usuario_nao_registrado(self):

        layout = [
            [sg.Text('Nome de usuário não encontrado.')],
            [sg.Text('Registre ele para acessar o sistema.')],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltarDoAviso2')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    # Metodo da janela de aviso de senha incorreta
    def janela_senha_incorreta(self):

        layout = [
            [sg.Text('Senha incorreta.')],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltarDoAviso3')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    # Metodo da janela da tabela dos grupos
    def janela_tabela(self):
    
        layout = [
            [sg.Text('', key='aviso_tabela', font='Verdana 12 bold', justification='left')],
            [sg.Image(filename="./fotos/grupos.png", size=(1280, 650))],
            [sg.Button('Grupo A', key='1', size=(11, 3)),
             sg.Button('Grupo B', key='2', size=(11, 3)),
             sg.Button('Grupo C', key='3', size=(11, 3)),
             sg.Button('Grupo D', key='4', size=(11, 3)),
             sg.Button('Grupo E', key='5', size=(11, 3)),
             sg.Button('Grupo F', key='6', size=(11, 3)),
             sg.Button('Grupo G', key='7', size=(11, 3)),
             sg.Button('Grupo H', key='8', size=(11, 3))],
            [sg.Button('Sair', font='Verdana 12 italic bold underline', key='voltar2')]
        ]

        return sg.Window('Tabela', layout=layout, element_justification='c', font='Verdana 12 italic bold',
                         finalize=True)

    # Metodo da janela dos jogos
    def janela_jogo(self, grupo):

        image = './fotos/bandeiras/grupo'
        vals = [['1', '2', '3', '4'], ['1', '3', '4', '2'], ['2', '3', '4', '1']]
        aposta = [['0', '0', '1', '1'], ['2', '2', '3', '3'], ['4', '4', '5', '5']]
        bets = [['0', '1'], ['2', '3'], ['4', '5']]
        tab = [0, 0, 0]

        for i in range(3):
            tab[i] = [
                [sg.Button('Estádio', key='estadio1' + str(i)),
                 sg.Button('',
                           image_filename=image + grupo + '/' + 'sel' + vals[i][0] + '.png', image_size=(200, 133),
                           image_subsample=2, border_width=0, key='time' + vals[i][0]),
                 sg.Input(key='aposta0' + aposta[i][0], size=(2, 1),font='Verdana 20 bold '),
                 sg.Text('x'),
                 sg.Input(key='aposta1' + aposta[i][1], size=(2, 1),font='Verdana 20 bold '),
                 sg.Button('',
                                   image_filename=image + grupo + '/' + 'sel' + vals[i][1] + '.png',
                                   image_size=(200, 133),
                                   image_subsample=2, border_width=0, key='time' + vals[i][1]),
                 sg.Text('R$'),
                 sg.Input(key='bet' + bets[i][0], size=(5, 1),font='Verdana 20 bold ')],
                [sg.Button('Estádio', key='estadio2' + str(i)),
                 sg.Button('',
                           image_filename=image + grupo + '/' + 'sel' + vals[i][2] + '.png', image_size=(200, 133),
                           image_subsample=2, border_width=0, key='time' + vals[i][2]),
                 sg.Input(key='aposta0' + aposta[i][2], size=(2, 1),font='Verdana 20 bold '),
                 sg.Text('x'),
                 sg.Input(key='aposta1' + aposta[i][3], size=(2, 1),font='Verdana 20 bold '),
                 sg.ReadFormButton('',
                                   image_filename=image + grupo + '/' + 'sel' + vals[i][3] + '.png',
                                   image_size=(200, 133),
                                   image_subsample=2, border_width=0, key='time' + vals[i][3]),
                 sg.Text('R$'),
                 sg.Input(key='bet' + bets[i][1], size=(5, 1),font='Verdana 20 bold ')]
            ]

        layout = [
            [sg.TabGroup([[
                sg.Tab('Primeira rodada', tab[0]),
                sg.Tab('Segunda Rodada', tab[1]),
                sg.Tab('Terceira Rodada', tab[2])]])],
            [sg.Text('', key='aviso_aposta', font='Verdana 10')],
            [sg.Button('Voltar', key='voltar3'), sg.Button('Apostar', key='apostar')]
        ]

        return sg.Window('Jogos do Grupo ' + grupo, layout=layout, finalize=True, element_justification='c',
                         font='Verdana 12 bold ')

    # Metodo da janela dos estadios
    def janela_estadio(self, id_do_jogo):
        
        self.estadio = Estadios()
        return self.estadio.GUI(id_do_jogo);

    # Metodo da janela das selecoes
    def janela_selecao(self, grupo, event):

        mixer.init()
        mixer.music.load(f'./hinos/grupo{grupo}/hino{event[4]}.mp3')  # cada grupo é um arquivo de 0 a 7 dentro os arquivos tem nome hino<i>.mp3 com i de 0 a 3
        nome_arquivo = f'./textos/selecoes/grupo{grupo}/text{event[4]}.txt'
        layout_info = Selecao(nome_arquivo).GUI()
        layout = [
            [sg.Image(f'./fotos/selecoes/grupo{grupo}/fot{event[4]}.png'),
             sg.Column(layout_info, vertical_alignment='top')],
            [sg.Text('Clique aqui para tocar o hino do país ->',font='Verdana 12 italic bold'),
            sg.Button('Play >',key='play',font='Verdana 10 underline'),
            sg.Button('Pause | |',key='pause',font='Verdana 10 underline')],
            [sg.Button('Voltar', key='voltar6')]
        ]

        return sg.Window('Seleção', layout=layout, finalize=True, element_justification='c')

