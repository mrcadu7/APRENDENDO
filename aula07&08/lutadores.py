class Lutador:
    
    def __init__(self, nome, nacionalidade, idade, altura,
                 peso, categoria, vitorias, derrotas, empates):
        
        self._nome = nome
        self._nacionalidade = nacionalidade
        self._idade = idade
        self._altura = altura
        self._peso = peso
        self._categoria = categoria
        self._vitorias = vitorias
        self._derrotas = derrotas
        self._empates = empates
        
    def apresentar(self):
        
        print(f'Lutador: {self._nome}')
        print(f'Origem: {self._nacionalidade}')
        print(f'{self._idade} anos de idade')
        print(f'{self._altura}m de altura')
        print(f'Pesando {self._peso}Kg')
        print(f'Ganhou: {self._vitorias}')
        print(f'Perdeu: {self._derrotas}')
        print(f'Empatou: {self._empates}')
        return
        
    
    def status(self):
        status_str = f'{self._nome}\n'
        status_str += f'Categoria: {self.categoria_pt}\n'
        status_str += f'{self._vitorias} vitórias\n'
        status_str += f'{self._derrotas} derrotas\n'
        status_str += f'{self._empates} empates\n'
        return print(status_str)
    
    def ganharLuta(self):
        self._vitorias += 1
    
    def perderLuta(self):
        self._derrotas += 1
    
    def empatarLuta(self):
        self._empates += 1
    
    
    @property
    def categoria_pt(self):
        if self._peso < 52.2:
            self._categoria = 'Inválido'
            
        elif self._peso < 70.3:
            self._categoria = 'Leve'
            
        elif self._peso < 83.9:
            self._categoria = 'Médio'
            
        elif self._peso < 120.2:
            self._categoria = 'Pesado'
            
        else:
            self._categoria = 'Inválido'
            
        return self._categoria