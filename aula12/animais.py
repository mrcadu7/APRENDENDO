from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, peso=None, idade=None, membros=None):
        self.__peso = peso
        self.__idade = idade
        self.__membros = membros
        
    @abstractmethod
    def locomover(self):
        pass
    
    @abstractmethod
    def alimentar(self):
        pass
    
    @abstractmethod
    def emitirSom(self):
        pass
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, novo_peso):
        self.__peso = novo_peso
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade
        
    @property
    def membros(self):
        return self.__membros
    
    @membros.setter
    def membros(self, novo_valor):
        self.__membros = novo_valor
    
    

class Mamifero(Animal):
    
    def __init__(self, corPelo=None, peso=None, idade=None, membros=None):
        super().__init__(peso, idade, membros)
        self.__corpelo = corPelo
           
    def locomover(self):
        return print('CORRENDO!')
    
    def alimentar(self):
        return print('MAMANDO!')
    
    def emitirSom(self):
        return print('SOM DE MAMIFERO UNHEEEEEE!')
    
    @property
    def corPelo(self):
        return self.__corpelo
    
    @corPelo.setter
    def corPelo(self, nova_cor):
        self.__corpelo = nova_cor
        
    
class Reptil(Animal):
    
    def __init__(self, corEscama=None, peso=None, idade=None, membros=None):
        super().__init__(peso, idade, membros)
        self.__corescama = corEscama     
        
    def locomover(self):
        return print('RASTEJANDO!')
    
    def alimentar(self):
        return print('COMENDO VEGETAIS!?')
    
    def emitirSom(self):
        return print('SOM DE REPTIL PSSSSSSSS!')
    
    @property
    def corEscama(self):
        return self.__corescama
    
    @corEscama.setter
    def corEscama(self, nova_cor):
        self.__corescama = nova_cor
    

class Peixe(Animal):
        
    def __init__(self, corEscama=None, peso=None, idade=None, membros=None):
        super().__init__(peso, idade, membros)  
        self.__corescama = corEscama
        
    def locomover(self):
        return print('NADANDO!')
    
    def alimentar(self):
        return print('COMENDO RESIDUOS!?')
    
    def emitirSom(self):
        return print('SOM DE PEIXE GLUBGLUB!')
    
    def soltarBolha(self):
        return print('SOLTOU UMA BOLHA!')
    
    
    @property
    def corEscama(self):
        return self.__corescama
    
    @corEscama.setter
    def corEscama(self, nova_cor):
        self.__corescama = nova_cor
    
    
class Ave(Animal):
    
    def __init__(self, corPena=None, peso=None, idade=None, membros=None):
        super().__init__(peso, idade, membros)
        self.__corpena = corPena
        
    def locomover(self):
        return print('VOANDO!')
    
    def alimentar(self):
        return print('COMENDO SEMENTES E FRUTAS!')
    
    def emitirSom(self):
        return print('SOM DE AVE PIIIIIU!')
    
    def fazerNinho(self):
        return print('CONSTRUIU UM NINHO!')
    

    @property
    def corPena(self):
        return self.__corpena
    
    @corPena.setter
    def corPena(self, nova_cor):
        self.__corpena = nova_cor
        
    
    
class Canguru(Mamifero):
        
    def locomover(self):
        return print('PULANDO!')
    
    def usarBolsa(self):
        return print('USANDO BOLSA!')
    

class Cachorro(Mamifero):
        
    def abanarRabo(self):
        return print('ABANANDO O RABO!')
    
    def enterrarOsso(self):
        return print('ENTERRANDO OSSO!')
    
    def emitirSom(self):
        return print('AU AU AU')

class Cobra(Reptil):
    pass
    
     
class Tartaruga(Reptil):
    
    def locomover(self):
        return print('ANNNNNDAAAANNNDOOO DEEEEEVAAAAAGAAAAARRR')
    
    
class Goldfish(Peixe):
    pass
               
        
class Arara(Ave):
    pass
        
        
    