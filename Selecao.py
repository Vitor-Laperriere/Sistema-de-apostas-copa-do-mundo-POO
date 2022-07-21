import PySimpleGUI as sg
import os
import random

# Classe que guarda informacoes sobre determinada selecao
class Selecao:

    # Construtor da classe
    def __init__(self, nome_arquivo):

        linhas = open(nome_arquivo, 'r').readlines()
        linhas = [linha[:-1] for linha in linhas]

        # Armazenando o nome do pais na variavel "pais"
        self.pais = ' '.join(linhas[0].split(' ')[1:])

        # Criando uma lista de jogadores da selecao 
        self.jogadores = []

        i = 2
        while linhas[i].split(' ')[0] != 'Texto:':
            # Armazenando o nome dos jogadores na lista "jogadores"
            self.jogadores.append(linhas[i])
            i += 1

        # Criando a variavel "texto"
        self.texto = ' '.join(linhas[i].split(' ')[1:])
        i += 1

        # Armazenando curiosidades sobre a selecao na variavel "texto"
        while i < len(linhas):
            self.texto += linhas[i]

    # Metodo que retorna uma lista com os nomes dos jogadores
    def acessar_jogadores(self):
        return self.jogadores

    # Metodo que retorna o nome do pais da selecao
    def acessar_pais(self):
        return self.pais
    
    # Metodo que retorna parametros para mostrar na interface grafica as informacoes da selecao
    def GUI(self):

        linha1 = [sg.Text(self.pais, font=("Helvetica", 25), text_color = "white")]
        linha2 = [sg.Text('\nJogadores:', font=("Helvetica", 14), text_color = "white")]
        linha3 = [sg.Column([[sg.Text(jogador)] for jogador in self.jogadores], scrollable = True, vertical_scroll_only = True, size = (None, 120))]
        linha4 = [sg.Text('\nDescrição:', font=("Helvetica", 14), text_color = "white")]
        linha5 = [sg.Text(self.texto, size = (30, None), font=("Helvetica", 12))]
        gui = [linha1, linha2, linha3, linha4, linha5]

        return gui