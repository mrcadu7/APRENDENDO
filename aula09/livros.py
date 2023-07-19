from publicacao import pubInterface

class Livro(pubInterface):
    from pessoas import Pessoa
    
    def __init__(self, titulo, autor, totpaginas, leitor:Pessoa, pagatual=0, aberto=False):
        self._titulo = titulo
        self._autor = autor
        self._totpaginas = totpaginas
        self._pagatual = pagatual
        self._aberto = aberto
        self._leitor = leitor
        
    def detalhes(self):
        detalhes_str = f'TÍTULO: {self._titulo}\n'
        detalhes_str += f'AUTOR: {self._autor}\n'
        detalhes_str += f'TOTAL DE PAGINAS: {self._totpaginas}\n'
        detalhes_str += f'PAGINA ATUAL: {self._pagatual}\n'
        detalhes_str += f'USADO? {self._aberto}\n'
        detalhes_str += f'DONO: {self._leitor._nome}\n'
        detalhes_str += f'IDADE: {self._leitor._idade}\n'
        detalhes_str += f'SEXO: {self._leitor._sexo}\n'
        return detalhes_str
    
    #INTERFACE    
    
    def abrir(self):
        self._aberto = True
    
    def fechar(self):
        self._aberto = False    
    
    def folhear(self, p):
        if p > self._totpaginas:
            self._pagatual = 0
        else:
            self._pagatual = p
    
    def avancarPag(self):
        self._pagatual += 1    
    
    def voltarPag(self):
        self._pagatual -= 1  
      
      
