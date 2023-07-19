from pessoass import Pessoa
from alunos import Aluno
from professores import Professor
from funcionarios import Funcionario

p1 = Pessoa()
p2 = Aluno()
p3 = Professor()
p4 = Funcionario()


p1.set_nome("Marcos")
p2.set_nome('Maria')
p3.set_nome('Fabio')
p4.set_nome('Giancarla')

p1.set_sexo('M')
p4.set_sexo('F')
p2.set_idade(18)

p2.set_curso('INFORMATICA')
p3.set_salario(2500)
p4.set_setor('ESTOQUE')

p1.status()
p2.status()
p3.status()
p4.status()

p2.receberAum(550)
