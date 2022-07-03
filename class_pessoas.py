from class_guias import Guia

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
