from pessoasss import Pessoas

class Visitante(Pessoas):
    
    def __init__(self, nome=None, idade=0, sexo=None):
        super().__init__(nome, idade, sexo)
    
    def fazerAniv(self):
        self._idade += 1
        
    def status(self):
        status_str = super().status()
        return status_str
    