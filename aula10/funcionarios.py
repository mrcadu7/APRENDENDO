from pessoass import Pessoa

class Funcionario(Pessoa):
    
    def __init__(self,  nome=None, idade=18, sexo=None, setor=None, trabalhando=None):
        super().__init__(nome, idade, sexo)
        
        self._setor = setor
        self._trabalhando = trabalhando
        
    def mudarTrabalho(self):
        self._trabalhando = not self._trabalhando
        
    #GETTER
    def get_setor(self):
        return self._setor
    
    #SETTER
    def set_setor(self, set):
        self._setor = set
        
    #GETTER
    def get_trabalhando(self):
        return self._trabalhando
    
    #SETTER
    def set_tabralhando(self, trab):
        self._trabalhando = trab