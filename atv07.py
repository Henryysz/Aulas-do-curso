nadadores = []
for num in range(3):
    nadadores.append(input('Nadador: '))
for colocacao, nadador in enumerate(nadadores, start=1):
    print('-' * 17)
    print(f'{colocacao}º lugar - {nadador.title()}')
