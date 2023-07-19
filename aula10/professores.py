from pessoass import Pessoa

class Professor(Pessoa):
    
    def __init__(self,  nome=None, idade=18, sexo=None, especialidade=None, salario=None):
        super().__init__(nome, idade, sexo)
        
        self._especialidade = especialidade
        self._salario = salario
        
    def receberAum(self, aum):
        self._salario += aum
        
    #GETTER
    def get_especialidade(self):
        return self._especialidade
    
    #SETTER
    def set_especialidade(self, espec):
        self._especialidade = espec
        
    #GETTER
    def get_salario(self):
        return self._salario
    
    #SETTER
    def set_salario(self, sal):
        self._salario = sal
        
    
    