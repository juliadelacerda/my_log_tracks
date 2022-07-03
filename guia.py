from pessoa import Pessoa
from trilha import Trilha

class Guia (Pessoa):
    def __init__ (self, nome, idade, endereco, valor_medio_trilha):
        super().__init__(nome, idade, endereco)
        self.valor_medio_trilha = valor_medio_trilha

    @property
    def valor_medio_trilha(self):
        return self.valor_medio_trilha

    @valor_medio_trilha.setter
    def valor_medio_trilha (self):
        return 'O valor médio da trilha não pode ser alterado'