def situacao_do_aluno(nota1: float, nota2: float) -> tuple:
    media = (nota1 +nota2) / 2
    situacao = 'Aprovado' if media > 6.9 else 'Reprovado'

    return media, situacao

media_aluno, situacao_academica = situacao_do_aluno(7, 8)
print(f'O aluno A obteve média {media_aluno:.1f} e está {situacao_academica}')
