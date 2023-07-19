from pessoasss import Pessoas

class Professor(Pessoas):
    
    def __init__(self, especialidade, salario, nome=None, idade=0, sexo=None):
        super().__init__(nome, idade, sexo)
        
        self._especialidade = especialidade
        self._salario = salario
        
    
    def receberAum(self, aumento):
        self._salario += aumento
        
    def fazerAniv(self):
        return super().fazerAniv()
        
    def status(self):
        return super().status()
    
    @property
    def especialidade(self):
        return self._especialidade
    
    @especialidade.setter
    def especialidade(self, nova_espec):
        self._especialidade = nova_espec
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario
    
    
    