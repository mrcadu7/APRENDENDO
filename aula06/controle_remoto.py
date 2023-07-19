class ControleRemoto:    
    
    def __init__(self, volume=50, ligado=False, tocando=False):
        self._volume = volume
        self._ligado = ligado
        self._tocando = tocando
        
        
    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False

    def abrirMenu(self):
        print('------- MENU -------')
        print(f'Está ligado? {self._ligado}')
        print(f'Está tocando? {self._tocando}')
        print(f'Volume: {self._volume}')
        for i in range(0, self._volume, 10):
            print("[]", end="")
        print('\n')
        return
            

        
    def fecharMenu(self):
        return print('Fechando MENU...')

    def maisVolume(self):
        if self._ligado:
            self._volume += 5
        else:
            return print(f'Aparelho desligado.. Impossível alterar VOLUME')

    def menosVolume(self):
        if self._ligado:
            self._volume -= 5
        else:
            return print(f'Aparelho desligado.. Impossível alterar VOLUME')

    def ligarMudo(self):
        if self._ligado and self._volume > 0:
            self._volume = 0
        else:
            return print(f'Aparelho desligado.. Impossível REPRODUZIR')

    def desligarMudo(self):
        if self._ligado and self._volume == 0:
            self._volume = 50
        else:
            return print(f'Aparelho desligado.. Impossível REPRODUZIR')

    def play(self):
        if self._ligado and not self._tocando:
            self._tocando = True
             

    def pause(self):
        if self._ligado and self._tocando:
            self._tocando = False

    '''@property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, v):
        self._volume = v'''
    
