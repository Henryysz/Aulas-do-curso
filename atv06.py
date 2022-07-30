vendedores = []
valores = []
tops = []

for num in range(1, 5):
    nome = input(f'{num}º vendedor: ')
    valor = float(input('Volume vendido: '))
    vendedores.append(nome)
    valores.append(valor)

tops = list(zip(valores, vendedores))
tops.sort(reverse=True)

print('-' * 20)
for valor, vendedor in tops[:2]:
    print(f'{vendedor} vendeu R${valor:.2f}')