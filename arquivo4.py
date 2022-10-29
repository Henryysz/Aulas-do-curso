from functools import reduce
#ATIVIDADE 1

numeros = [ num for num in range(1, 21)]
print(list(filter(lambda num: num % 2 == 0, numeros)))

#ATIVIDADE 2

numeros = [ num for num in range(30, 51)]
print(list(filter(lambda num: num % 2 != 0, numeros)))

#ATIVIDADE 3

numeros = [ num for num in range(-10, 10)]
print(list(filter(lambda num: num < 0, numeros)))

#ATIVIDADE 4

numeros = [num for num in range(1, 11)]

menor = reduce((lambda x, y: x if (x < y) else y), numeros)
print(menor)

#ATIVIDADE 5

nomes = ['gabriel','allan','camila','gisele','henry',]
print(list(map(lambda letra: letra.title(), nomes)))

#ATIVIDADE 6

nomes = ['gabriel','allan','camila','gisele','henry',]
nomes.sort(key=lambda letras: letras[1], reverse=False)
print(nomes)

#ATIVIDADE 7

nome = ['gabriel','allan','camila','gisele','henry',]
nome.sort(key=lambda letras: letras[1], reverse=True)
print(nome)

#ATIVIDADE 8

numero = [ num for num in range(1, 21)]
print(list(map(lambda num: num * 10 if num % 2 == 0 else round(num / 3, 2), numero)))

