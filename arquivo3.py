numeros = [ num for num in range(1, 21)]
print(list(filter(lambda num: num % 2 == 0, numeros)))

print(f'Números ímpares: {list(filter(lambda num: num % 2 == 1, numeros))}')

print(f'Maiores que 10: {list(filter(lambda num: num > 10, numeros))}')

def numeros_impares(numeros):
    if numeros %2 !=0:
        return numeros
    else:
        return
    
print(list(map(numeros_impares, numeros)))
