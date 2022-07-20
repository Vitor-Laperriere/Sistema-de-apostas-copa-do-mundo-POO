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

    def acessar_jogadores(self):
        return self.jogadores

    def acessar_pais(self):
        return self.pais
    
    def GUI(self):

        linha1 = [sg.Text(self.pais, font=("Helvetica", 25), text_color = "white")]
        linha2 = [sg.Text('\nJogadores:', font=("Helvetica", 14), text_color = "white")]
        linha3 = [sg.Column([[sg.Text(jogador)] for jogador in self.jogadores], scrollable = True, vertical_scroll_only = True, size = (None, 120))]
        linha4 = [sg.Text('\nDescrição:', font=("Helvetica", 14), text_color = "white")]
        linha5 = [sg.Text(self.texto, size = (30, None), font=("Helvetica", 12))]
        gui = [linha1, linha2, linha3, linha4, linha5]

        return gui


