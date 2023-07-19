from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, peso=None, idade=None, membros=None):
        self.__peso = peso
        self.__idade = idade
        self.__membros = membros
        
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
    
    def emitirSom(self):
        return print('SOM DE MAMIFERO UNHEEEEEE!')
    
    @property
    def corPelo(self):
        return self.__corpelo
    
    @corPelo.setter
    def corPelo(self, nova_cor):
        self.__corpelo = nova_cor
        

class Lobo(Mamifero):
    def emitirSom(self):
        return print('AU AU AU')


class Cachorro(Lobo):
    
    
    def emitirSom(self):
        return print('AU AU AU')
    
    '''#Polomorfia de Sobrecarga:
    def reagir(self, frase:str):
        if frase == 'toma comida' or 'ola':
            return print('Abanar o rabo e latir')
        else:
            return print('ROSNAR!')
    
    def reagir(self, hora:int):
        if hora <12:
            return print('Abanar')
        elif hora >=18:
            return print('ignorar')
        else:
            return print('Abanar rabo e latir!')
    
    def reagir(self, dono:bool):
        if dono:
            return print('abanar o rabo')
        else:
            return print('ROSNAR E LATIR!')
    
    def reagir(self, idade:int, peso:float):
        if idade <5:
            if peso <10:
                return print('abanar')
            else:
                return print('latir')
        else:
            if peso <10:
                return print('rosnar')
            else:
                return print('ignorar') '''   #esse conceito não funciona para o python,
                                              #é aconselhado a usar condicionais e blablabla

#EXEMPLO USANDO CONDICIONAIS PARA EQUIPARAR AO OVERCHARGE

    def reagir(self, frase=None, hora=None, dono=None, idade=None, peso=None):
        if frase is not None:
            if frase == 'toma comida' or frase == 'ola':
                return print('Abanar o rabo e latir')
            else:
                return print('ROSNAR!')
        elif hora is not None:
            if hora < 12:
                return print('Abanar')
            elif hora >= 18:
                return print('ignorar')
            else:
                return print('Abanar rabo e latir!')
        elif dono is not None:
            if dono:
                return print('abanar o rabo')
            else:
                return print('ROSNAR E LATIR!')
        elif idade is not None and peso is not None:
            if idade < 5:
                if peso < 10:
                    return print('abanar')
                else:
                    return print('latir')
            else:
                if peso < 10:
                    return print('rosnar')
                else:
                    return print('ignorar')
    