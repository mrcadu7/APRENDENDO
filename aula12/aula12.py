from animais import *

'''m = Mamifero('Azul')
r = Reptil('Azul')
p = Peixe('Azul')
a = Ave('Azul')

m.peso = 85.3
m.idade = 2 
m.membros = 4
print(f'{m.peso}Kg \n{m.idade} anos \n{m.membros} membros')
m.locomover()
m.alimentar()
m.emitirSom()

print('-----------------------')

p.peso = 10
p.idade = 1 
p.membros = 0
print(f'{p.peso}Kg \n{p.idade} anos \n{p.membros} membros')
p.locomover()
p.alimentar()
p.emitirSom()
p.soltarBolha()

print('-----------------------')

a.peso = 0.89
a.idade = 3
a.membros = 2 #eu sei que ta errado, só didatico
print(f'{a.peso}Kg \n{a.idade} anos \n{a.membros} membros')
a.locomover()
a.alimentar()
a.emitirSom()
a.fazerNinho()

print('-----------------------')


r.peso = 5
r.idade = 4
r.membros = 4
print(f'{r.peso}Kg \n{r.idade} anos \n{r.membros} membros')
a.locomover()
a.alimentar()
a.emitirSom()'''


m = Mamifero()
c = Canguru()
k = Cachorro()

m.peso = 5.7
m.idade = 8
m.membros = 4
print(f'{m.peso}Kg \n{m.idade} anos \n{m.membros} membros')
m.locomover()
m.alimentar()
m.emitirSom()

print('-----------------')

c.peso = 78
c.idade = 15
c.membros = 4
print(f'{c.peso}Kg \n{c.idade} anos \n{c.membros} membros')
c.locomover()
c.alimentar()
c.emitirSom()
c.usarBolsa()


print('-----------------')

k.peso = 12
k.idade = 5
k.membros = 4
print(f'{k.peso}Kg \n{k.idade} anos \n{k.membros} membros')
k.locomover()
k.alimentar()
k.emitirSom()
k.enterrarOsso()
k.abanarRabo()

