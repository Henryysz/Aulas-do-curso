def soma (a: int, b: int):
    '''Esse código realizará a soma dos dois números, "a" e "b", e depois mostrará o resultado.'''
    resultado = a + b
    return resultado

def subtracao(a: int,b: int):
    '''Esse código realizará a subtração dos dois números, "a" e "b", e depois mostrará o resultado.'''
    resultado = a - b
    return resultado

def multiplicacao(a: int,b: int):
    '''Esse código realizará a multiplicação dos dois números, "a" e "b", e depois mostrará o resultado.'''
    resultado = a * b
    return resultado

def divisao(a : int,b : int):
    '''Esse código realizará a soma dos dois números, "a" e "b", e mostrará o resultado.'''
    if a == 0 or b == 0:
        return f'Operação inviável'
    resultado = a / b
    return resultado
    


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

