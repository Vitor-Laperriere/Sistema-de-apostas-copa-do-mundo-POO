import csv
import pandas as pd
from fpdf import FPDF
from Usuario import Usuario


class Sistema:
    arquivo_usuarios = f'./users.csv'

    def __init__(self):

        self.tabela = pd.read_csv(self.arquivo_usuarios, sep=',')

    def usuario_registrado(self, usuario):

        for i in self.tabela.index:
            if self.tabela['nome'][i] == usuario.nome:  # and\
                # self.tabela['senha'][i] == usuario.senha and\
                # self.tabela['saldo'][i] == usuario.saldo and\
                # self.tabela['id'][i] == usuario.ind:
                return True

        return False

    def login_valido(self, usuario):

        for i in self.tabela.index:

            if str(self.tabela['nome'][i]) == usuario.nome and \
                    str(self.tabela['senha'][i]) == usuario.senha:
                usuario.ind = int(self.tabela['id'][i])
                usuario.saldo = int(self.tabela['saldo'][i])

                return True

        return False

    def registrar_usuario(self, usuario):

        #   Caso onde usuario ja foi registrado
        if self.usuario_registrado(usuario):
            return

        f = open(self.arquivo_usuarios, 'a', newline='\n')
        writer = csv.writer(f)
        linha = [str(usuario.ind), usuario.nome, usuario.senha, str(usuario.saldo)]
        writer.writerow(linha)
        f.close()

        self.tabela = pd.read_csv(self.arquivo_usuarios, sep=',')

    def escreve_recibo(self, usuario, apostas):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        vals = [[0, 1, 2, 3], [0, 2, 3, 1], [1, 2, 3, 0]]

        file = open('./textos/selecoes.txt', 'r')

        usuario.saldo = 0

        num_do_jogo = int(0)
        for grupo in range(8):
            foi_apostado = [apostas[i].aposta_realizada for i in range(num_do_jogo, num_do_jogo + 6)]
            if not any(foi_apostado):
                num_do_jogo += 6
                linha = file.readline()
                continue

            proximo_texto_pdf = '-' * 150
            pdf.cell(200, 10, txt=proximo_texto_pdf, ln=1, align='C')
            proximo_texto_pdf = 'Grupo ' + chr(grupo + ord('A'))
            pdf.cell(200, 10, txt=proximo_texto_pdf, ln=1, align='C')
            proximo_texto_pdf = '-' * 150
            pdf.cell(200, 10, txt=proximo_texto_pdf, ln=1, align='C')
            linha = file.readline()
            selecoes = linha.split(',')

            for rodada in range(3):
                if apostas[num_do_jogo].aposta_realizada:
                    proximo_texto_pdf = selecoes[vals[rodada][0]] + ' ' + str(
                        apostas[num_do_jogo].palpite_sel_1) + ' x ' + str(apostas[num_do_jogo].palpite_sel_2) + ' ' + \
                                        selecoes[vals[rodada][1]]
                    print(proximo_texto_pdf)
                    pdf.cell(200, 10, txt=proximo_texto_pdf, ln=0, align='L')
                    proximo_texto_pdf = 'R$' + str(apostas[num_do_jogo].dinheiro_apostado)
                    print(proximo_texto_pdf)
                    pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='R')
                    usuario.adicionar_saldo(int(apostas[num_do_jogo].dinheiro_apostado))
                num_do_jogo += 1

                if apostas[num_do_jogo].aposta_realizada:
                    proximo_texto_pdf = selecoes[vals[rodada][2]] + ' ' + str(
                        apostas[num_do_jogo].palpite_sel_1) + ' x ' + str(apostas[num_do_jogo].palpite_sel_2) + ' ' + \
                                        selecoes[vals[rodada][3]]
                    print(proximo_texto_pdf)
                    pdf.cell(200, 10, txt=proximo_texto_pdf, ln=0, align='L')
                    proximo_texto_pdf = 'R$ ' + str(apostas[num_do_jogo].dinheiro_apostado)
                    print(proximo_texto_pdf)
                    pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='R')
                    usuario.adicionar_saldo(int(apostas[num_do_jogo].dinheiro_apostado))
                num_do_jogo += 1

        proximo_texto_pdf = 150 * "-"
        pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='C')

        proximo_texto_pdf = usuario.nome
        pdf.cell(0, 10, txt=proximo_texto_pdf, ln=0, align='L')

        proximo_texto_pdf = 'Total à pagar R$' + str(usuario.saldo)
        pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='R')

        pdf.output(usuario.nome + ".pdf")

        return


if __name__ == '__main__':

    s = Sistema()
    otavio = Usuario('Otavio', '12', 2, 1)

    s.registrar_usuario(otavio)

    if s.login_valido(otavio):
        print("Login :)")
    else:
        print("Sem Login :(")
