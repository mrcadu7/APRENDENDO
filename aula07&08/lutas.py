from lutadores import Lutador
from random import randint
class Luta:
    
    def __init__(self, desafiado:Lutador, desafiante:Lutador, round, aprovada=False):
        
        self._desafiado = desafiado
        self._desafiante = desafiante
        self._round = round
        self._aprovada = aprovada

    def marcarLuta(self, lut1:Lutador, lut2:Lutador):
        
        if lut1.categoria_pt == lut2.categoria_pt and lut1 != lut2:
            self._aprovada = True
            self._desafiado = lut1
            self._desafiante = lut2
            
            return print('LUTA APROVADA!')
        else:
            self._aprovada = False
            self._desafiado = None
            self._desafiante = None
            return print('LUTA DESAPROVADA!')
           
    
    def lutar(self):
        
        if self._aprovada:
            print('CHEGOU A HORA DA VERDADE!')
            print('### DESAFIADO ###')
            self._desafiado.apresentar()
            print('##################')
            print('### DESAFIANTE ###')
            self._desafiante.apresentar()
            print('##################')
            vencedor = randint(0,2)
            
            if vencedor == 0:
                self._desafiado.empatarLuta()
                self._desafiante.empatarLuta()
                return print('A luta EMPATOU!')
            
            if vencedor == 1:
                self._desafiado.ganharLuta()
                self._desafiante.perderLuta()
                return print(f'{self._desafiado._nome} GANHOU a luta!')
            
            if vencedor == 2:
                self._desafiante.ganharLuta()
                self._desafiado.perderLuta()
                return print(f'{self._desafiante._nome} GANHOU a luta!')       
            
                                
        else:
            return print(f'Luta não pode acontecer!')
    