#SUPERCLASSE
class Pessoa:
    
    def __init__(self, nome=None, idade=0, sexo=None):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
        
    def fazerAniv(self):
        self._idade += 1
        
    def status(self):
        status_str = f'NOME: {self._nome}\n'
        status_str += f'IDADE: {self._idade}\n'
        status_str += f'SEXO: {self._sexo}\n'
        return print(status_str)
    
    # Getter para o atributo "nome"
    def get_nome(self):
        return self._nome

    # Setter para o atributo "nome"
    def set_nome(self, nn):
        self._nome = nn

    # Getter para o atributo "idade"
    def get_idade(self):
        return self._idade

    # Setter para o atributo "idade"
    def set_idade(self, ni):
        self._idade = ni

    # Getter para o atributo "sexo"
    def get_sexo(self):
        return self._sexo

    # Setter para o atributo "sexo"
    def set_sexo(self, ns):
        self._sexo = ns