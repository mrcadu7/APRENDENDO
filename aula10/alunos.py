from pessoass import Pessoa

class Aluno(Pessoa):
    
    def __init__(self, nome=None, idade=18, sexo=None, matricula=None, curso=None):
        super().__init__(nome, idade, sexo)

        
        self._matricula = matricula
        self._curso = curso
        
    def cancelarMatr(self):
        return print('MATRICULA SERÁ CANCELADA!')
    
    #GETTER
    def get_matricula(self):
        return self._matricula
    
    #SETTER
    def set_matricula(self, matr):
        self._matricula = matr
    
    #GETTER
    def get_curso(self):
        return self._curso
    
    #SETTER
    def set_curso(self, cur):
        self._curso = cur