class Cachorro:
    def __init__(self, nome, raça, cor):
        self.nome = nome
        self.raca = raça
        self.cor = cor

    def latir(self):
        return 'auau'
    
    def andar(self):
        return f'{self.nome} está andando pela casa.'
    
    def fazer_festa(self):
        return f'{self.nome} quebrou um vaso, sujou o chão de terra e balançou o rabo esperando um elogio.'
    
class Gatos:
    def __init__(self, nome, raça, cor):
        self.nome = nome
        self.raca = raça
        self.cor = cor

    def miar(self):
        return 'MIAU - em tradução literal, me alimente'
    
    def andar(self):
        return f'{self.nome} está andando pela casa e derrubando todas as coisas em locais altos.'

    def brincar(self):
        return f'{self.nome} está brincando com a bola de lã, bastante entretido'