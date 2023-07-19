from banco import ContaBanco

p1 = ContaBanco(11111, 'cc','Foque')
p1.abrirConta()
p1.depositar(10000000)
print(p1.estadoAtual())


'''p2 = ContaBanco(222222, 'cp', 'Walter')
p2.abrirConta()
p2.sacar(150)
p2.fecharConta()
print(p2.estadoAtual())'''

