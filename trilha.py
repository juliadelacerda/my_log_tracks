from class_pessoas import Pessoa

class Trilha:
    def __init__ (self, distancia_total, grau_dificuldade, nome, localizacao):
        self.distancia_total = distancia_total
        self.grau_dificuldade = grau_dificuldade # facil, medio ou dificil
        self.nome = nome
        self.localizacao = localizacao
        self.pessoa = Pessoa

        @property 
        def distanciaTotal (self):
            return self.distancia_total

        @distancia_total.setter
        def distanciaTotal (self):
            return 'Não foi possível alterar a distância total'

        @property
        def grauDificuldade (self):
            return self.grau_dificuldade

        @grau_dificuldade.setter
        def grauDificuldade (self):
            return 'Não foi possível alterar o grau de dificuldade'

        @property
        def nome (self):
            return self.nome

        @nome.setter
        def nome (self):
            return "Não foi possível alterar o nome"

        @property
        def localizacao (self):
            return self.localizacao

        @localizacao.setter
        def localizacao (self):
            return "Não foi possível alterar a localização"

        