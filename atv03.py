numeros = []
for num in range(1, 11):
    numero = int(input(f'{num}º número: '))
    numeros.append(numero)

print(f'Maior número lido: {max(numeros)}')
print(f'Menor número lido: {min(numeros)}')