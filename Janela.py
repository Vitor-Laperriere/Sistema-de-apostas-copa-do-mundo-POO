class Janela:

    def janela_login(self):

        layout = [
            [sg.Text('Usuário'), sg.Input(key='user', size=(20,1))],
            [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20,1))],
            [sg.Button('Registrar', font='Verdana 14 italic bold underline'),
            sg.Button('Entrar', font='Verdana 14 italic bold underline')],
        ]

        return sg.Window('Login', layout=layout, finalize=True, font='Verdana 14 italic bold', element_justification='c')

    def janela_usuario_ja_registrado(self):

        layout = [
            [sg.Text('Nome de usuário já registrado.')],
            [sg.Text('Tente outro.')],
            [sg.Button('Voltar',font='Verdana 12 italic bold underline', key='voltarDoAviso')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold', element_justification='c')

    def janela_usuario_nao_registrado(self):

        layout = [
            [sg.Text('Nome de usuário não encontrado.')],
            [sg.Text('Registre ele para acessar o sistema.')],
            [sg.Button('Voltar',font='Verdana 12 italic bold underline', key='voltarDoAviso2')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold', element_justification='c')

    def janela_senha_incorreta(self):

        layout = [
            [sg.Text('Senha incorreta.')],
            [sg.Button('Voltar',font='Verdana 12 italic bold underline', key='voltarDoAviso3')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold', element_justification='c')


    def janela_tabela(self):

        layout = [
            [sg.Image(filename="./fotos/grupos.png",size=(1280,650))],
            [sg.Button('Grupo A', key='1', size=(11,3)),
            sg.Button('Grupo B', key='2', size=(11,3)),
            sg.Button('Grupo C', key='3', size=(11,3)),
            sg.Button('Grupo D', key='4', size=(11,3)),
            sg.Button('Grupo E', key='5', size=(11,3)),
            sg.Button('Grupo F', key='6', size=(11,3)),
            sg.Button('Grupo G', key='7', size=(11,3)),
            sg.Button('Grupo H', key='8', size=(11,3))],
            [sg.Button('Voltar',font='Verdana 12 italic bold underline', key='voltar2')]
        ]

        return sg.Window('Tabela',layout = layout,element_justification='c',font='Verdana 12 italic bold',finalize = True)

    def janela_jogo(self,grupo):
        
        image = './fotos/bandeiras/grupo'

        vals =   [['1','2','3','4'],['1','3','4','2'],['2','3','4','1']]
        aposta = [['0','0','1','1'],['2','2','3','3'],['4','4','5','5']]
        bets = [['0','1'],['2','3'],['4','5']]
        tab = [0, 0, 0]

        for i in range(3):

            tab[i] = [
                [sg.Button('',button_color = sg.TRANSPARENT_BUTTON,
                image_filename = image + grupo + '/' + 'sel' + vals[i][0] + '.png' , image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][0]),
                sg.Input(key='aposta0' + aposta[i][0], size=(3,1)),
                sg.Input(key='aposta1' + aposta[i][1], size=(3,1)),
                sg.ReadFormButton('',button_color = sg.TRANSPARENT_BUTTON,
                image_filename = image + grupo + '/' + 'sel' + vals[i][1] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][1]),sg.Input(key='bet' + bets[i][0], size=(7,1)),
                sg.Button('Estádio',key='estadio1' + str(i))],
                [sg.Button('',button_color = sg.TRANSPARENT_BUTTON,
                image_filename = image + grupo + '/' + 'sel' + vals[i][2] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][2]),
                sg.Input(key='aposta0' + aposta[i][2], size=(3,1)),
                sg.Input(key='aposta1' + aposta[i][3], size=(3,1)),
                sg.ReadFormButton('',button_color = sg.TRANSPARENT_BUTTON,
                image_filename = image + grupo + '/' + 'sel' + vals[i][3] + '.png', image_size=(50,33), image_subsample=2, border_width=1,key='time' + vals[i][3]),sg.Input(key='bet' + bets[i][1], size=(7,1)),
                sg.Button('Estádio',key='estadio2'+str(i))] 
            ]


        layout = [
            [sg.TabGroup([[
            sg.Tab('Primeira rodada', tab[0]),
            sg.Tab('Segunda Rodada', tab[1]),
            sg.Tab('Terceira Rodada', tab[2])]])],
            [sg.Button('Voltar', key='voltar3'), sg.Button('Apostar', key='apostar')]
        ]

        return sg.Window('Jogos do Grupo ' + grupo ,layout = layout,finalize = True, element_justification='c')


    def janela_estadio(self, id_do_jogo):

        self.estagio = Estadios()
        return self.estagio.GUI(id_do_jogo);

    def janela_selecao(self, grupo, event):

        #mixer.init()
        #mixer.music.load('hinos/grupo' + grupo + '/' + 'hino' + event[4])  # cada grupo é um arquivo de 0 a 7 dentro os arquivos tem nome hino<i>.mp3 com i de 0 a 3
        nome_arquivo = f'./textos/selecoes/grupo{grupo}/text{event[4]}.txt'
        layout_info = Selecao(nome_arquivo).GUI()
        layout = [
            [sg.Image(f'./fotos/selecoes/grupo{grupo}/fot{event[4]}.png'), 
            sg.Column(layout_info, vertical_alignment = 'top')], 
            [sg.Button('Voltar', key='voltar6')]
        ]

        return sg.Window('Seleção', layout = layout, finalize = True, element_justification='c')