from lutadores import Lutador
from lutas import Luta

l = []
l.append(Lutador('Pretty Boy', 'França', 31, 1.75, 68.9, 'Leve', 11, 2, 1))
l.append(Lutador('Putscript', 'Brasil', 29, 1.68, 57.8, 'Leve', 14, 2, 3))
l.append(Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9, 'Médio', 12, 2, 1))
l.append(Lutador('Dead Code', 'Austrália', 28, 1.93, 81.6, 'Médio', 13, 0, 2))
l.append(Lutador('Ufocobol', 'Brasil', 37, 1.70, 119.3, 'Pesado', 5, 4, 3))
l.append(Lutador('Nerdaard', 'EUA', 30, 1.81, 105.7, 'Pesado', 12, 2, 4))


uec01 = Luta(l[0],l[5],0)
uec01.marcarLuta(l[0],l[5])
uec01.lutar()

#l[0].status()
