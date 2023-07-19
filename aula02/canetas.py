class Caneta:
    
    def __init__(self, cor, ponta, carga, tampar=True):
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampar = tampar
    
    def status(self):
        status_str = f'Uma caneta de cor {self.cor}\n'
        status_str += f'Está tampada: {self.tampar}\n'
        status_str += f'Sua ponta é {self.ponta}\n'
        status_str += f'Está com {self.carga}% de carga\n'
        return status_str
        
    
    def tampar(self):
        self.tampar = True
        
    
    def destampar(self):
        self.tampar = False
        
    
    def rabiscar(self):
        if self.tampar == True:
            return 'ERRO! Não é possível com a tampa fechada!'          
        else:
            return 'RABISCANDO..'
    
    def teste(self):
        return 'Penis!'
    

    
    