class Produto:
    def __init__(self, nome, preco, categoria, descricao):
        self.nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.descricao = descricao

    @property
    def preco(self):
        '''Retorna o preço do produto.'''
        return f'{self.__preco:.2f}'

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            print('Valor inválido!')
            return self.__preco
        self.__preco = novo_preco
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nova_categoria):
        self.__categoria = nova_categoria


    def reajustar_preco(self, percentual):
        self.preco = self.__preco + self.__preco * (percentual / 100)
        return f'Preço reajustado em {percentual}% com sucesso.'

    def __repr__(self):
        return f'{self.nome} - {self.categoria}'

    def __str__(self):
        return f'Sou o seu objeto - {self.nome}'

if __name__ == '__main__':
    print('Favor executar o arquivo de cadastro de produtos.')


