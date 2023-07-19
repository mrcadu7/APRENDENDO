class Pessoa:
    
    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
        
    def fazerAniver(self):
        self._idade += 1
        
    @property
    def get_nome(self):
        return self._nome
    
    @property
    def get_idade(self):
        return self._idade
    
    @property
    def get_sexo(self):
        return self._sexo