import csv
import os

import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF

# Classe que gerencia os usuarios do sistema e gera o recibo das apostas
class Sistema:

    # Caminho para o arquivo de usuarios
    arquivo_usuarios = f'./users.csv'

    # Construtor da classe
    def __init__(self):
        # Armazenando o banco de usuarios em uma tabela
        self.tabela = pd.read_csv(self.arquivo_usuarios, sep=',')

    # Metodo que retorna verdadeiro se um usuario estiver registrado
    def usuario_registrado(self, usuario):

        for i in self.tabela.index:
            if self.tabela['nome'][i] == usuario.nome:
                return True

        return False

    # Metodo que retorna verdadeiro se um login for valido
    # Ou seja, o nome do usuario e a senha devem estar condizentes
    def login_valido(self, usuario):

        # Iterando sobre a tabela de usuarios
        for i in self.tabela.index:
            # Verificando se o nome do usuario e a senha sao encontrados na tabela
            if str(self.tabela['nome'][i]) == usuario.nome and \
                    str(self.tabela['senha'][i]) == usuario.senha:
                usuario.ind = int(self.tabela['id'][i])
                usuario.saldo = int(self.tabela['saldo'][i])

                return True

        return False

    # Metodo que registra um usuario no banco de usuarios
    def registrar_usuario(self, usuario):

        # Caso onde usuario ja foi registrado
        if self.usuario_registrado(usuario):
            return

        # Escrevendo o nome usuario no arquivo de usuarios
        f = open(self.arquivo_usuarios, 'a', newline='\n')
        writer = csv.writer(f)
        linha = [str(usuario.ind), usuario.nome, usuario.senha, str(usuario.saldo)]
        writer.writerow(linha)
        f.close()

        self.tabela = pd.read_csv(self.arquivo_usuarios, sep=',')

        return

    # Metodo que cria um pdf com senha que contem as apostas de um usuario
    def escreve_recibo(self, usuario, apostas):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        vals = [[0, 1, 2, 3], [0, 2, 3, 1], [1, 2, 3, 0]]

        file = open('./textos/selecoes.txt', 'r')

        usuario.saldo = 0

        num_do_jogo = int(0)
        for grupo in range(8): # loop que escreve todos os grupos no arquivo recibo
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
                    
                    pdf.cell(200, 10, txt=proximo_texto_pdf, ln=0, align='L')
                    proximo_texto_pdf = 'R$' + str(apostas[num_do_jogo].dinheiro_apostado)
                    
                    pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='R')
                    usuario.adicionar_saldo(int(apostas[num_do_jogo].dinheiro_apostado))
                num_do_jogo += 1

                if apostas[num_do_jogo].aposta_realizada:
                    proximo_texto_pdf = selecoes[vals[rodada][2]] + ' ' + str(
                        apostas[num_do_jogo].palpite_sel_1) + ' x ' + str(apostas[num_do_jogo].palpite_sel_2) + ' ' + \
                                        selecoes[vals[rodada][3]]
                    
                    pdf.cell(200, 10, txt=proximo_texto_pdf, ln=0, align='L')
                    proximo_texto_pdf = 'R$ ' + str(apostas[num_do_jogo].dinheiro_apostado)
                    
                    pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='R')
                    usuario.adicionar_saldo(int(apostas[num_do_jogo].dinheiro_apostado))
                num_do_jogo += 1

        proximo_texto_pdf = 150 * "-"
        pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='C')

        proximo_texto_pdf = usuario.nome
        pdf.cell(0, 10, txt=proximo_texto_pdf, ln=0, align='L')

        proximo_texto_pdf = 'Total à pagar R$' + str(usuario.saldo)
        pdf.cell(0, 10, txt=proximo_texto_pdf, ln=1, align='R')

        pdf.output(usuario.nome + '1'+ ".pdf") #crio um pdf sem criptografia

        # abro ele com a biblioteca de criptografia
        file = PdfFileReader(usuario.nome + '1'+ ".pdf")

        out = PdfFileWriter() #crio um objeto de escrita
        num = file.numPages     #percorro suas páginas
        for idx in range(num):

            page = file.getPage(idx)

            #e adiciono nesse objeto
            out.addPage(page)

        # encripto o objeto com a senha do usuário
        out.encrypt(usuario.senha)

        with open(usuario.nome + ".pdf", "wb") as f:

            # Gero o pdf a partir desse arquivo criptografado que criei
            out.write(f)

        os.remove(usuario.nome + '1'+ ".pdf")  # removo o antigo não criptografado

        return


