from alunoss import Aluno

class Bolsista(Aluno):
    def __init__(self, nome=None, idade=0, sexo=None, matricula=0, curso=None, bolsa=0):
        super().__init__(nome, idade, sexo, matricula, curso)
        
        self._bolsa = bolsa
        
    def renovarBolsa(self):
        pass
    
    #sobreposição
    def pagarMens(Aluno):
        return print('Mensalidade paga com desconto de bolsista!')
    
    def fazerAniv(self):
        self._idade += 1
        
    def status(self):
        status_str = super().status()
        return status_str
    
    @property
    def bolsa(self):
        return self._bolsa
    
    @bolsa.setter
    def bolsa(self, nova_bolsa):
        self._bolsa = nova_bolsa
    
    
    
    
    
    