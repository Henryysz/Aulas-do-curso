turma = {}
dados_aluno = {}
notas = []

for _ in range(2):
    nome = input('Digite seu nome: ')

    for num in range(1, 5):
       nota = float(input(f'Digite a {num}ª nota: '))
       notas.append(nota)

    dados_aluno['Notas'] = nota
    dados_aluno['Média'] = sum(notas) / len(notas)
    dados_aluno['Maior nota'] = max(notas)
    dados_aluno['Menor nota'] = min(notas)
    situacao = 'Aprovado' if dados_aluno['Média'] > 6.99 else 'Reprovado'
    dados_aluno['Situação'] = situacao
    turma[nome] = dados_aluno.copy()
    dados_aluno.clear()

aprovados = []
medias = []


print('-' * 30)
for nome, dados in turma.items():
    if dados["Média"] > 6.99:
        aprovados.append(nome)
        medias.append(dados["Média"])

alunos_aprovados = list(zip(medias, aprovados))
alunos_aprovados.sort(reverse=True)

for pos, alunos in enumerate(alunos_aprovados, start=1):
    nome, media = alunos
    print(pos, nome, media, sep = ' - ')