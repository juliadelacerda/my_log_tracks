class Pessoa:
    def __init__ (self,nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    # @property
    # def tipo (self):
    #     return self.tipo

    # @tipo.setter
    # def tipo (self):
    #     rai_se ValueError('O tipo não pode ser alterado!')


    @property 
    def nome (self):
        return self._nome

    @nome.setter 
    def nome (self, novo_nome):
        self._nome = novo_nome

    @property
    def idade (self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade


    @property
    def endereco (self):
        return self._endereco

    @endereco.setter
    def endereco (self, novo_endereco):
        self._endereco = novo_endereco


class Amigos(Pessoa):
    def __init__ (self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)


class Familia(Pessoa):
    def __init__ (self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)


class Guia(Pessoa):
    def __init__ (self, nome, idade, endereco, novo_nome_medio_trilha):
        super().__init__(nome, idade, endereco)
        self.novo_nome_medio_trilha = novo_nome_medio_trilha

    @property
    def novo_nome_medio_trilha(self):
        return self._novo_nome_medio_trilha


    @novo_nome_medio_trilha.setter
    def novo_nome_medio_trilha (self, novo_novo_nome):
        self._novo_nome_medio_trilha = novo_novo_nome