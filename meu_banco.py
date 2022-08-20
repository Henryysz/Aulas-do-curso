class ContaCorrente:

    def __init__(self, titular, saldo= 900):
        self.titular = titular
        self.__saldo = saldo
        self.extrato = []
      
    def consulta_saldo(self):
        return f'{self.__saldo:.2f}'
    
    def extratos(self):
        print('EXTRATO - 2022')
        print('-' * 30)
        for mov in self.extrato:
            print(mov)
        print('-' * 30)

    def sacar(self, valor):
        if valor > self.__saldo:
            return f'Saldo insuficiente. Saldo disponível: {self.__saldo:.2f}'
        self.__saldo -= valor
        self.extrato.append(f'-{valor:.2f}')
        return 'Saque realizado com sucesso!'

    def depositar(self, valor):
        self.__saldo -= valor
        self.extrato.append(f'+{valor:.2f}')

    def transferir(self, destino, valor):
        if valor > self.__saldo:
            return f'Saldo insuficiente. Saldo disponível: {self.__saldo:.2f}'
        self.sacar(valor)
        destino.depositar(valor)
        self.extrato.append(f'-{valor:.2f}')
        return 'Depósito realizado com sucesso!' 
    