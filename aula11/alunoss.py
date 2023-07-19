from pessoasss import Pessoas

class Aluno(Pessoas):
    def __init__(self, nome=None, idade=0, sexo=None, matricula=0, curso=None):
        super().__init__(nome, idade, sexo)
        
        self._matricula = matricula
        self._curso = curso
    
    
    def pagarMens(self):
        return print('Mensalidade paga!')

    def fazerAniv(self):
        self._idade += 1
        
    def status(self):
        status_str = super().status()
        return status_str
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, nova_matricula):
        self._matricula = nova_matricula
        
    @property
    def curso(self):
        return self._curso
    
    @matricula.setter
    def curso(self, novo_curso):
        self._curso = novo_curso
        
    