from random import randint

def gera_matricula(tamanho: int) -> int:
    matricula = []
    for _ in range(tamanho):
        matricula.append(str(randint(1,9)))
    matricula = ''.join(matricula)
    return int(matricula)

    if __name__ == '__main__':
        print('Esse arquivo é um módulo')