from livros import Livro
from pessoas import Pessoa

p = []
p.append(Pessoa('Pedro', 22, 'M'))
p.append(Pessoa('Maria', 25, 'F'))

l = []
l.append(Livro('Aprendendo Python', 'Jose da Silva', 300, p[0]))
l.append(Livro('POO para iniciantes', 'Pedro Paulo', 500, p[1]))
l.append(Livro('Python Avançado', 'Maria Candido', 800, p[0]))

#print(l[0].detalhes()) 
l[1].abrir()
l[1].folhear(200)
l[1].avancarPag()
print(l[1].detalhes()) 