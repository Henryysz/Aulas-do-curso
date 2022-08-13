''' Testes para o uso de módulos de funções matemáticas básicas, aula do dia 13/08/2022'''
from wsgiref.validate import validator


def soma(num1: int, num2: int) -> int:
    '''Realiza a soma entre dois números inteiros, podendo ser iguais ou distintos.'''
    result = num1 + num2
    return result

def subtracao(num1: int, num2: int) -> int:
    '''Realiza a subtração entre dois números inteiros, podendo ser iguais ou distintos.'''
    result = num1 - num2
    return result

def multiplicacao(num1: int, num2: int) -> int:
    '''Realiza a multiplicação entre dois números inteiros, podendo ser iguais ou distintos.'''
    result = num1 * num2
    return result

def divisao(num1: int, num2: int) -> int:
    '''Realiza a divisão entre dois números inteiros, podendo ser iguais ou distintos'''
    if num1 == 0 or num2 == 0:
        return f'Operação inviável.'
    result = num1 / num2
    return result

def media(numeros: list) -> float:
    '''Cria uma lista com os números recebidos, e retorna a média entre eles'''
    return sum(numeros) / len(numeros)

def calcular_percentual(valor: float, percentual: int, decimal: int) -> float:
    result = (valor * percentual) / 100
    return f'{result:.{decimal}f}'

def par_ou_impar(numero: int) -> int:
    '''Serve para apontar se o número é ímpar ou par.'''
    if numero % 2 == 0:
        result = 'É par.'
    else:
        result = 'É ímpar.'
    return result

def fatorial(numero: int) -> int:
    '''Serve para multiplicar o número pelos números anteiores a ele, parando no 1.'''
    fat = 1
    for num in range(numero, 0, -1):
        fat *= num
    return fat

def potencia(base: int, expoente: int) -> int:
    '''Serve para elevar um número à potência escolhida.'''
    resultado = base ** expoente
    return resultado

def quantos_porcento(numero: int, num_final: int) -> float:
    '''Serve para mostrar a porcentagem de um número com relação ao número total.'''
    porcentagem = (numero * 100) / num_final
    return f'{porcentagem:.2f}%'








