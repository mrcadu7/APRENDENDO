from abc import ABC, abstractmethod

class Pessoa(ABC):
    
    def __init__(self, nome='None', idade:int=0, sexo:str='None', experiencia=0):
        
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__experiencia = experiencia
        
    def status(self):
        status_str = f'NOME: {self.nome}\n'
        status_str += f'IDADE: {self.idade}\n'
        status_str += f'SEXO: {self.sexo}\n'
        status_str += f'EXPERIENCIA: {self.experiencia}\n'
        return status_str
        
    @abstractmethod
    def _ganharExp(self):
        pass
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, novo_sexo):
        self.__sexo = novo_sexo
        
    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, nova_experiencia):
        self.__experiencia = nova_experiencia


class Gafanhoto(Pessoa):
    
    def __init__(self, login='None', totassist=0, nome='None', idade:int=0, sexo:str='None', experiencia=0):
        super().__init__(nome, idade, sexo, experiencia)
        
        self._login = login
        self._totassist = totassist
        
    def viuMaisUm(self):
        self.totassist + 1
    
    def _ganharExp(self):
        self.experiencia += 1
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, novo_login):
        self._login = novo_login
        
    @property
    def totassist(self):
        return self._totassist
    
    @totassist.setter
    def totassist(self, novo_totassist):
        self._totassist = novo_totassist