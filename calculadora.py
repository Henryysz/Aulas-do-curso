from matematica import (
    soma,
    subtracao,
    divisao,
    multiplicacao
    )

op: str = input('Que operação deseja [-+/*]?: ')
num1 = int(input('1º Número: '))
num2 = int(input('2º Número: '))

if op == '+':
    print(f'Soma dos números: {soma(num1, num2)}')
elif op == '-':
    print(f'Subtração dos números: {subtracao(num1, num2)}')
elif op == '*':
    print(f'Multiplicação dos números: {multiplicacao(num1, num2)}')
elif op == '/':
    print(f'Divisão dos números: divisao: {divisao(num1, num2)}')

