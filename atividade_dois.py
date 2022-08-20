class Aula:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class ContaCorrente:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo 
        
