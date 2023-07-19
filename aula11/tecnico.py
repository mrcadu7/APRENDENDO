from alunoss import Aluno

class Tecnico(Aluno):
    
    def __init__(self, regProf, nome=None, idade=0, sexo=None, matricula=0, curso=None):
        super().__init__(nome, idade, sexo, matricula, curso)
        
        self._regprof = regProf
    
    def praticar(self):
        return (f'{self._nome} está Praticando!')
         
        
    @property
    def regProf(self):
        return self._regprof
    
    @regProf.setter
    def regProf(self, novo_regProf):
        self._regprof = novo_regProf