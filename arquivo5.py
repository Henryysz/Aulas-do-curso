numeros = [num for num in range(1, 21)]


def par_ou_impar(numeros):
    if numeros %2==0:
        return numeros * 2
    else:
        return numeros / 2
        
print(list(map(par_ou_impar, numeros)))

print(list(map(lambda num: num * 2 if num % 2 == 0 else num / 2, numeros)))