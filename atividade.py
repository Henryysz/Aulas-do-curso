from random import randint

numero_secreto = randint(1, 100)
palpite = int(input('Palpite: '))
contador = 0

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print('O número é maior!')
    elif palpite > numero_secreto:
        print('O número é menor!')
    palpite = int(input('Novo palpite: '))
    contador +=1
else:
    print('Parabéns, você acertou!')
    print(f'Número de tentativas: {contador}')