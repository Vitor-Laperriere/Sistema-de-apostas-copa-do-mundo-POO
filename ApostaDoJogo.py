# Classe que armazena informacoes de uma determinada aposta de um jogo
class ApostaDoJogo:

    #   Construtor da classe ApostaDoJogo
    def __init__(self, id_do_jogo):
        self.aposta_realizada = False
        self.id_do_jogo = id_do_jogo
        self.palpite_sel_1 = -1
        self.palpite_sel_2 = -1
        self.dinheiro_apostado = -1

    #   Funcao que cria uma aposta de um determinado jogo
    def definir_aposta(self, p1, p2, d):
        self.aposta_realizada = True
        self.palpite_sel_1 = p1
        self.palpite_sel_2 = p2
        self.dinheiro_apostado = d
        #print(f"Setei os valores {p1}, {p2} e {d}")

    #   Funcao que remove uma aposta de um determinado jogo.
    def remover_aposta(self):
        self.aposta_realizada = False
        self.palpite_sel_1 = -1
        self.palpite_sel_2 = -1
        self.dinheiro_apostado = -1
