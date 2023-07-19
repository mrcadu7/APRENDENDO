class ContaBanco:
    
    def __init__(self, numconta, tipo, dono, saldo=0, status=False):
        self.numconta = numconta
        self.__tipo = tipo
        self._dono = dono
        self._saldo = saldo
        self._status = status
        
    def estadoAtual(self):
        print(f'CONTA: {self.numconta}')
        print(f'TIPO: {self.__tipo}')
        print(f'DONO: {self._dono}')
        print(f'SALDO: R${self._saldo}')
        print(f'STATUS: {self.status_pt}')
        print(f'-------------------------------')
    
    def abrirConta(self):
        self._status = True
        if self.__tipo  == "cc":
            self._saldo = 50
        elif self.__tipo  == "cp":
            self._saldo = 150          
        print('CONTA ABERTA COM SUCESSO!')
    
    def fecharConta(self):
        if self._saldo > 0:
            print('CONTA COM DINHEIRO! AÇÃO NÃO REALIZADA!')
        elif self._saldo <0:
            print('CONTA EM DÉBITO! AÇÃO NÃO REALIZADA!')
        else:
            self._status = False
            
    
    def depositar(self, v):
        if self._status == True:
            self._saldo = self._saldo + v
        else:
            print('IMPOSSÍVEL DEPOSITAR! CONTA FECHADA OU NÃO EXISTE!')

    
    def sacar(self, v):
        if self._status == True:
            if self._saldo >= v:
                self._saldo = self._saldo - v
            else:
                print('SALDO INSUFICIENTE!')
        else:
            print('IMPOSSíVEL SACAR! CONTA NÃO EXISTE!')
            
    
    def pagarMensal(self):
        v = 0
        
        if self.__tipo == "cc":
            v = 12
        elif self.__tipo == "cp":
            v = 20
        
        if self._status == True:    
            if self._saldo > v:
                self._saldo = self._saldo - v
            else:
                print('SALDO INSUFICIENTE!')
        else:
            print('IMPOSSíVEL PAGAR! CONTA NÃO EXISTE!')
    
    
    @property
    def status_pt(self):
        if self._status:
            return "ATIVO"
        else:
            return "INATIVO"
    
    '''#Getters
    
    @property
    def numconta(self):
        return self.numconta
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def dono(self):
        return self._dono
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def status(self):
        return self._status
    
        
    #Setters
    
    @numconta.setter
    def numconta(self, n):
        self.numconta = n
        
    @tipo.setter
    def tipo(self, t):
        self.__tipo = t
    
    @dono.setter
    def dono(self, d):
        self._dono = d
        
    @saldo.setter
    def dono(self, s):
        self._saldo = s
    
    @status.setter
    def status(self, s):
        self._status = s'''
    
    
    