from selecao import *

class jogo:

    def __init__(self, nome_arquivo):
        linhas = open(nome_arquivo, 'r').readlines()
        linhas = [linha[:-1] for linha in linhas]
        
        self.selecoes = [selecao(f'arquivos/{linhas[1]}.txt'), selecao(f'arquivos/{linhas[2]}.txt')]

        self.data = linhas[3].split(' ')[1]

        self.horario = ' '.join(linhas[4].split(' ')[1:])

        self.local = ' '.join(linhas[5].split(' ')[1:])


    def get_gui(self):
        guis_selecoes = [selecao_da_vez.get_gui() for selecao_da_vez in self.selecoes]

        gui = [[sg.Column(guis_selecoes[0]), sg.Column(guis_selecoes[1])]]

        print(gui)
        
        return gui

if __name__ == '__main__':
    layout = jogo('arquivos/jogo1.txt').get_gui()

    window = sg.Window('Teste', layout)

    while True:
        event, value = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    window.close()
