class Usuario:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

        #getter
        @property
        def login(self):
            return self.__login

        #setter
        @login.setter
        def login(self, novo_login):
            self.__login = novo_login

        @property
        def senha(self):
            return self.__senha

        @senha.setter
        def senha(self, nova_senha):
            if len(nova_senha) < 4:
                print('Senha inválida. Tamanho mínimo de 4')
            self.__senha = nova_senha
            return 'Senha alterada com sucesso'
