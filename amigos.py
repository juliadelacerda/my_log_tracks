from pessoa import Pessoa

class Amigos(Pessoa):
    def __init__ (self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)
