from people import Gafanhoto
from videos import Video

class Visualizacao(Gafanhoto, Video):
    
    def __init__(self, espectador:Gafanhoto, filme:Video):
        super().__init__()
        self._espectador = espectador
        self._filme = filme
        self._espectador.totassist = self._espectador.totassist + 1
        self._filme.views = self._filme.views + 1
        
        
    def status(self):
        status_str = f'NOME: {self._espectador.nome}\n'
        status_str += f'IDADE: {self._espectador.idade}\n'
        status_str += f'SEXO: {self._espectador.sexo}\n'
        status_str += f'EXPERIENCIA: {self._espectador.experiencia}\n'
        status_str += f'TITULO: {self._filme.titulo}\n'
        status_str += f'Avaliações: {self._filme.avaliacao}\n'
        status_str += f'Views: {self._filme.views}\n'
        status_str += f'Curtidas: {self._filme.curtidas}\n'
        status_str += f'Reproduzindo: {self._filme.reproduzindo}\n'
        return status_str
    
    def avaliar(self, nota=None, porc=None):
        if nota is not None:
            self._filme.avaliacao = nota
        elif porc is not None:
            if porc <= 20:
                self._filme.avaliacao = 3
            elif porc <= 50:
                self._filme.avaliacao = 5
            elif porc <= 90:
                self._filme.avaliacao = 8
            else:
                self._filme.avaliacao = 10
    