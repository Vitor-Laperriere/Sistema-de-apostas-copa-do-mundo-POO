from PySimpleGUI import PySimpleGUI as sg
from Usuario import Usuario
from Sistema import Sistema
from Selecao import Selecao
from Estadios import Estadios
from ApostaDoJogo import ApostaDoJogo
from Janela import Janela
import os
import time
from pygame import mixer



if __name__ == '__main__':

    sg.theme('DarkRed')

    J = Janela()
    janela = 8 * [None]
    janela[0] = J.janela_login()

    grupo = '1'
    apostas = 48 * [None]

    for i in range(0, 48):
        apostas[i] = ApostaDoJogo(i)

    sistema = Sistema()
    usuario = Usuario()

    musica_tocando = 0

    while True:

        window, event, values = sg.read_all_windows()
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

        if window == janela[0]:
            janela[0]['aviso_registro'].update('')
            usuario.nome = str(values['user'])
            usuario.senha = str(values['senha'])
            usuario.saldo = 0

            if event == 'Entrar' and not sistema.usuario_registrado(usuario):

                janela[0].hide()
                janela[6] = J.janela_usuario_nao_registrado()

            elif event == 'Entrar' and not sistema.login_valido(usuario):

                janela[0].hide()
                janela[7] = J.janela_senha_incorreta()

            elif event == 'Entrar' and sistema.login_valido(usuario):

                janela[0].hide()
                janela[1] = J.janela_tabela()
                janela[1]['aviso_tabela'].update(f"Bem vindo, {usuario.nome}")

            elif event == 'Registrar' and not sistema.usuario_registrado(usuario):
                #janela atualiza mostrando que o usuario foi registrado
                janela[0]['aviso_registro'].update('Registro feito')
                usuario.ind = int(time.time())
                sistema.registrar_usuario(usuario)

            elif event == 'Registrar' and sistema.usuario_registrado(usuario):

                janela[0].hide()
                janela[5] = J.janela_usuario_ja_registrado()

        if window == janela[1] and event != 'voltar2':
            janela[1].hide()
            grupo = event
            janela[2] = J.janela_jogo(grupo)

        if window == janela[2] and event == 'apostar' or 'time' in event or 'estadio' in event:

            jogo = int(grupo) - 1
            num_do_jogo = int(jogo * 6)

            if event == 'apostar':
                print("aposta realizada")

                for i in range(6):
                    palpites = [values['aposta0' + str(i)], values['aposta1' + str(i)]]
                    valor_aposta = values['bet' + str(i)]
                    if (palpites[0].isdigit() and palpites[
                        1].isdigit() and valor_aposta.isdigit()):  # esse if impede que insira apostas inválidas
                        apostas[num_do_jogo].definir_aposta(palpites[0], palpites[1], valor_aposta)

                    num_do_jogo += 1

            sistema.escreve_recibo(usuario, apostas)

            if 'time' in event:
                janela[2].hide()
                janela[3] = J.janela_selecao(grupo, event)

            if 'estadio1' in event:
                if event[8] == '0':
                    pass
                elif event[8] == '1':
                    num_do_jogo = num_do_jogo + 2
                else:
                    num_do_jogo = num_do_jogo + 4

                print(num_do_jogo)
                janela[2].hide()
                janela[4] = J.janela_estadio(num_do_jogo)

            if 'estadio2' in event:
                if event[8] == '0':
                    num_do_jogo = num_do_jogo + 1
                elif event[8] == '1':
                    num_do_jogo = num_do_jogo + 3
                else:
                    num_do_jogo = num_do_jogo + 5

                print(num_do_jogo)
                janela[2].hide()
                janela[4] = J.janela_estadio(num_do_jogo)

        if window == janela[3] and event == 'play':
            mixer.music.play()
            musica_tocando = 1

        if window == janela[3] and event == 'pause':

            if (musica_tocando == 0):
                mixer.music.unpause()
                musica_tocando = 1

            elif (musica_tocando):
                mixer.music.pause()
                musica_tocando = 0

        if window == janela[3] and event == 'voltar6':
            janela[3].hide()
            janela[2].un_hide()

        if window == janela[4] and event == 'voltar5':
            janela[4].hide()
            janela[2].un_hide()

        if window == janela[5] and event == 'voltarDoAviso':
            janela[5].hide()
            janela[0].un_hide()

        if window == janela[6] and event == 'voltarDoAviso2':
            janela[6].hide()
            janela[0].un_hide()

        if window == janela[7] and event == 'voltarDoAviso3':
            janela[7].hide()
            janela[0].un_hide()
