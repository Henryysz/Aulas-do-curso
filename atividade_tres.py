class ContaCorrente:
    CONSULTAS = 0
    TAXA_CONSULTAR_SALDO = 1

    def __init__(self, titular, saldo = 500):
        self.agencia = '001'
        self.titular = titular
        self.__saldo = saldo
    
    def consultar_saldo(self):
        
        ContaCorrente.CONSULTAS +=1
        if ContaCorrente.CONSULTAS > 2:
            self.__saldo -= ContaCorrente.TAXA_CONSULTAR_SALDO
            print(f'Você foi tarifado em R${ContaCorrente.TAXA_CONSULTAR_SALDO}')
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor > self.__saldo:
            return f'Saldo insuficiente. Saldo disponível: {self.__saldo}'
        self.__saldo -= valor
        return 'Saque realizado com sucesso!'

    def transferir(self, destino, valor):
        if valor > self.__saldo:
            return f'Saldo insuficiente. Saldo disponível: {self.__saldo}'
        self.sacar(valor)
        destino.depositar(valor) 
        return 'Depósito realizado com sucesso!'   
