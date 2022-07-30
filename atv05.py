numeros = []
for num in range(10):
    number = int(input('Número: '))
    numeros.append(number)

numeros.sort()
print(f'Em ordem crescente: {numeros}')
numeros.sort(reverse=True)
print(f'Em ordem decrescente: {numeros}')
