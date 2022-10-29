from functools import reduce

numeros = [12, 43, 3224, 3, 123, 483, 999, 13, 44, 1000]

menor = reduce((lambda x, y: x if (x < y) else y), numeros)
print(menor)

resultado = reduce((lambda x, y: x * y), numeros)
saida = (f'{resultado:,.2f}')
resultado_formatado = saida.translate(saida.maketrans({',':'.', '.':'.'}))
print(resultado_formatado)