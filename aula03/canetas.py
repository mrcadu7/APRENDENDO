class Caneta:
    
    def __init__(self, cor, ponta, carga, tampar=True):
        
        
        self.cor = cor
        self._ponta = ponta
        self.__carga = carga
        self.__tampada = tampar
    
    def status(self):
        print(f'Uma caneta de cor {self.cor}')
        print(f'Está tampada: {self.__tampada}')
        print(f'Sua ponta é {self._ponta}')
        print(f'Está com {self.__carga}% de carga')
        return
    
    def tampar(self):
        self.__tampada = True
        
    
    def destampar(self):
        self.__tampada = False
        
    
    def rabiscar(self):
        if self.__tampada == True:
            print('ERRO! Não é possível com a tampa fechada!')            
        else:
            print('RABISCANDO..')
    
    def teste(self):
        print('Penis!')
    

    
    