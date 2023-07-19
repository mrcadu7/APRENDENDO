from visitante import Visitante
from alunoss import Aluno
from bolsista import Bolsista
from professores import Professor
from tecnico import Tecnico

v1 = Visitante()
v1.nome = "pedro"
v1.idade = 234
v1.sexo = 'gay'
v1.status()

a1 = Aluno()
a1.nome = 'Joao'
a1.matricula = 1111
a1.curso = 'Informatica'
a1.idade = 16
a1.sexo = 'M'
a1.pagarMens()
a1.status()

b1 = Bolsista()
b1.nome = 'Claudio'
b1.matricula = 2222
b1.bolsa = 12.5
b1.sexo = 'M'
b1.pagarMens()

p1 = Professor('Matematica', 2200)
p1.nome = 'Pedro'
p1.idade = 45
p1.sexo = 'M'
p1.status()
print(p1.especialidade)
print(p1.salario)

t1 = Tecnico(0)
t1.regProf = 22352
t1.nome = 'Tigauin'
t1.idade = 27
t1.sexo = 'F'
t1.status()
print(t1.praticar())


