from pessoa import Pessoa

class Trilha:
    def __init__ (self, distancia_total, grau_dificuldade, nome, localizacao):
        self.distancia_total = distancia_total
        self.grau_dificuldade = grau_dificuldade # facil, medio ou dificil
        self.nome = nome
        self.localizacao = localizacao
        self.pessoa = Pessoa

        @property 
        def distancia_total (self):
            return self._distancia_total

        @distancia_total.setter
        def distancia_total (self, nova_distancia_total):
            self._distancia_total = nova_distancia_total


        @property
        def grau_dificuldade (self):
            return self._grau_dificuldade

        @grau_dificuldade.setter
        def grau_dificuldade (self, novo_grauDificuldade):
            self._grau_dificuldade = novo_grauDificuldade


        @property
        def nome (self):
            return self._nome

        @nome.setter
        def nome (self, novo_nome_trilha):
            self._nome = novo_nome_trilha

        
        @property
        def localizacao (self):
            return self._localizacao

        @localizacao.setter
        def localizacao (self, nova_localizacao):
            self._localizacao = nova_localizacao
        