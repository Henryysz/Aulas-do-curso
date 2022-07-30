pares = []
impares = []
for num in range(1, 11):
    numero = int(input(f'{num}º número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Pares lidos: {len(pares)}')
print(f'Maior par lido: {max(pares)}')
print(f'Menor par lido: {min(pares)}\n')
print(f'Ímpares lidos: {len(impares)}')
print(f'Maior ímpar lido: {max(impares)}')
print(f'Menor ímpar lido: {min(impares)}')