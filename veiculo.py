class Veiculo:
    def __init__(self, fabricante,  modelo, motor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.motor = motor
        self.velocidade = 0
        self.ligado = False

    def ligar_veiculo(self):
        self.ligado = not self.ligado
        if self.ligado:
            return f'Veículo ligado'
        return 'Veículo desligado'

    def parar_veiculo(self):
        if self.ligado:
            return 'Veículo parado'
        return 'Veículo já está parado'

class Carro(Veiculo):
    def __init__(self, fabricante, modelo, motor, cor, cambio = 'Automático'):
        super().__init__(fabricante, modelo, motor)
        self.cor = cor
        self.cambio = cambio
    
    def parar_veiculo(self):
        if self.ligado:
            return 'Carro estacionado'
        return 'Carro já está parado'


