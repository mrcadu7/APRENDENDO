from abc import ABC, abstractmethod

class Pessoas(ABC):
    
    def __init__(self, nome=None, idade=0, sexo=None):
        
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
    
    @abstractmethod
    def fazerAniv(self):
        self._idade += 1
    
    @abstractmethod
    def status(self):
        status_str = f'Nome: {self._nome}\n'
        status_str += f'Idade: {self._idade}\n'
        status_str += f'Sexo: {self._sexo}\n'
        return print(status_str)
    
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade
    
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, novo_sexo):
        self._sexo = novo_sexo
        
    
    