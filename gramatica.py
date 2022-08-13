'''Serve para mostrar algumas funções para uso gramatical, no caso contar quantidade de letras, entre outras funções.'''

def conta_letras(palavra: str) -> int:
    '''Mostra a quantidade de letras na frase ou nome que forem inseridos.'''
    contador = 0

    for ch in palavra:
        if ch == " ":
            continue
        contador +=1

    return contador

if __name__ == '__main__':
    print('Isso é apenas um módulo')