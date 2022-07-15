import PySimpleGUI as sg
import os
import random

class Selecao:

    def __init__(self, nome_arquivo):

        linhas = open(nome_arquivo, 'r').readlines()
        linhas = [linha[:-1] for linha in linhas]

        self.pais = ' '.join(linhas[0].split(' ')[1:])
        self.jogadores = []

        i = 2
        while linhas[i].split(' ')[0] != 'Texto:':
            self.jogadores.append(linhas[i])
            i += 1

        self.texto = ' '.join(linhas[i].split(' ')[1:])
        i += 1

        while i < len(linhas):
            self.texto += linhas[i]
    
    def GUI(self):

        linha1 = [sg.Text(self.pais)]
        linha2 = [sg.Text('Elenco:')]
        linha3 = [sg.Column([[sg.Text(jogador)] for jogador in self.jogadores], scrollable = True, vertical_scroll_only = True)]
        linha4 = [sg.Text(self.texto, size = (60, None))]
        gui = [linha1, linha2, linha3, linha4]

        return gui


if __name__ == '__main__':
    arquivos = os.listdir('./texto_selecoes')

    layout1 = Selecao(f'./texto_selecoes/grupo7/text3.txt').GUI()
    #layout2 = selecao(f'./texto_selecoes/grupo7/text2.txt').GUI()
    #layout1 = selecao(f'./texto_selecoes/grupo7/{random.choice(arquivos)}').GUI()
    #layout2 = selecao(f'./texto_selecoes/grupo7/{random.choice(arquivos)}').GUI()

    layout = [[sg.Image(f'./fotos_selecoes/grupo7/fot1.png'), sg.Column(layout1, vertical_alignment = 'top')]]
    #layout = [[sg.Column(layout1, vertical_alignment = 'top'), sg.Column(layout2, vertical_alignment = 'top')]]


    window = sg.Window('Teste', layout)

    while True:
        event, value = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    window.close()
