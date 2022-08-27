class Mamifero:

    def emitir_som(self):
        return 'Mamifero emitindo som'

    def se_locomover(self):
        return 'Mamifero se locomovendo'

class Cachorro(Mamifero):
    def __init__(self, nome, raça, cor):
        self.nome = nome
        self.raca = raça
        self.cor = cor

    def emitir_som(self):
        return 'auau'
    
    def se_locomover(self):
        return f'{self.nome} está andando pela casa.'
    
    def fazer_festa(self):
        return f'{self.nome} quebrou um vaso, sujou o chão de terra e balançou o rabo esperando um elogio.'
    
class Gatos(Mamifero):
    def __init__(self, nome, raça, cor):
        self.nome = nome
        self.raca = raça
        self.cor = cor

    def emitir_som(self):
        return 'MIAU - em tradução literal, me alimente'
    
    def se_locomover(self):
        return f'{self.nome} está andando pela casa e derrubando todas as coisas em locais altos.'

    def brincar(self):
        return f'{self.nome} está brincando com a bola de lã, bastante entretido'