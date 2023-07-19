from interface import AcoesVideo

class Video(AcoesVideo):
    
    def __init__(self, titulo='Titulo', avaliacao=0, views=0,
                 curtidas=0, reproduzindo=False):
        super().__init__()
        
        self._titulo = titulo
        self._avaliacao = avaliacao
        self._views = views
        self._curtidas = curtidas
        self._reproduzindo = reproduzindo
        
    def status(self):
        status_str = f'TITULO: {self.titulo}\n'
        status_str += f'Avaliações: {self.avaliacao}\n'
        status_str += f'Views: {self.views}\n'
        status_str += f'Curtidas: {self.curtidas}\n'
        status_str += f'Reproduzindo: {self.reproduzindo}\n'
        return status_str
    
    def play(self):
        self.reproduzindo = True
    
    def pause(self):
        self.reproduzindo = False
    
    def like(self):
        self.curtidas += 1 
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo
        
    @property
    def avaliacao(self):
        return self._avaliacao
    
    @avaliacao.setter
    def avaliacao(self, nova_aval):
        nova = (self._avaliacao + nova_aval)/self._views
        self._avaliacao = nova
    
    @property
    def views(self):
        return self._views
    
    @views.setter
    def views(self, novas_views):
        self._views = novas_views
        
    @property
    def curtidas(self):
        return self._curtidas
    
    @curtidas.setter
    def curtidas(self, novas_curtidas):
        self._curtidas = novas_curtidas
    
    @property
    def reproduzindo(self):
        return self._reproduzindo
    
    @reproduzindo.setter
    def reproduzindo(self, estado):
        self._reproduzindo = estado