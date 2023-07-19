from videos import Video
from people import Gafanhoto
from visualizacao import Visualizacao

videos = []

videos .extend([Video('Aula 1 de POO'), Video('Aula 12 de PHP'), Video('Aula de Hentai')]) #retorna pela classe caso eu desejar status da classe


'''print(v[0].status())'''

g = [Gafanhoto(nome='pedrin', idade=22, sexo='M'),
     Gafanhoto(nome='Walteru-kun', idade=29, sexo='?' )]
g[0]._ganharExp()

'''print(g.status())'''

vis1 = Visualizacao(g[0], videos[1])
vis2 = Visualizacao(g[1], videos[2])
vis1.avaliar(porc=71)

print(vis1.status())
print('-*'*15)
print(vis2.status())

