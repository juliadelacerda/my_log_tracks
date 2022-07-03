class Pessoa:
    def __init__ (self, tipo, nome, idade, endereco):
        self.tipo = tipo #Guia, amigo ou familia
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    @property
    def tipo (self):
        return self.tipo

    @tipo.setter
    def tipo (self):
        if self.tipo == 'guia':
            self.tipo = Guia
            return self.tipo == Guia
        
        elif self.tipo == 'amigos':
            self.tipo = Amigos
            return self.tipo == Amigos
        
        elif self.tipo == 'familia':
            self.tipo = Familia
            return self.tipo == Amigos


    @property 
    def nome (self):
        return self.nome

    @nome.setter 
    def nome (self, nome):
        raise ValueError("O nome não pode ser alterado")

    @property
    def idade (self):
        return self.idade
    
    @idade.setter
    def idade(self):
        raise ValueError("A idade não pode ser alterada")

    @property
    def endereco (self):
        return self.endereco

    @endereco.setter
    def endereco (self):
        raise ValueError ("O endereço não pode ser alterado")




class Guia (Pessoa):
    def __init__ (self, nome, idade, endereco, valor_medio_trilha):
        super().__init__(nome, idade, endereco)
        self.valor_medio_trilha = valor_medio_trilha

    @property
    def valor_medio_trilha(self):
        return self.valor_medio_trilha

    @valor_medio_trilha.setter
    def valor_medio_trilha (self):
        raise ValueError ('O valor médio da trilha não pode ser alterado')


class Amigos(Pessoa):
    def __init__ (self, nome, idade, endereco):
        super().__init__(nome, idade, endereco)


class Familia(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(self, nome, idade, endereco)

