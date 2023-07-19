class Caneta:
    
    def __init__(self, modelo, ponta):
        
        self.modelo = modelo
        self.ponta = ponta
        
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def ponta(self):
        return self._ponta
    
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @ponta.setter
    def ponta(self, ponta):
        self._ponta = ponta
    
    def status(self):
        print('SOBRE A CANETA:')
        print(f'MODELO: {self.modelo}')
        print(f'PONTA: {self.ponta}')
    
    