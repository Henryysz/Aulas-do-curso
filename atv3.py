lista_nome = []
lista_peso = []
lista_altura = []
def calculo_do_IMC(infos: list) -> None:
    for info in infos:
        nomes, peso, altura = info
        imc = peso / (altura ** 2)
        print(f'{nome.title()} : IMC = {round(imc, 2)}')
    ...

for num in range(1):
    nome: str = input('nome: ')
    lista_nome.append(nome)
    peso: float = float(input('peso: '))
    lista_peso.append(peso)
    altura: float = float(input('Altura: '))
    lista_altura.append(altura)
    
dados = list(zip(lista_nome, lista_peso, lista_altura))

calculo_do_IMC(dados)

