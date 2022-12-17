import threading


class Poltrona:
    def __init__(self):
        self.client = None
        self.semaphore = threading.Semaphore()

    def reserva(self, client) -> bool:
        self.semaphore.acquire()
        if self.client is None:
            self.client = client

            self.semaphore.release()
            return True
        else:
            self.semaphore.release()
            return False


class Aviao:
    def __init__(self, n=30):
        self.poltronas = [Poltrona() for _ in range(n)]

    def livres(self) -> list[bool]:
        res = []
        for p in self.poltronas:
            p.semaphore.acquire()
            res.append(p.client is None)
            p.semaphore.release()

        return res
    
    def reserva(self, poltronas_desejadas, identificador):
        retorno = [] # Lista com True para sucesso e False para fracasso.

        for indice in poltronas_desejadas:
            poltrona = self.poltronas[indice]
            poltrona.semaphore.acquire()
            if poltrona.client is None:
                poltrona.client = identificador
                poltrona.semaphore.release()
                retorno.append(True)
            else:
                poltrona.semaphore.release()
                retorno.append(False)

        return retorno
