notas = []
for indice in range(1, 5):
    nota = float(input(f'Digite a {indice}ª nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f'Média: {media:.2f}')
if media >=7:
    print('Aprovado!')
elif media < 5:
    print('Reprovado!')
else:
    print('Em recuperação!')