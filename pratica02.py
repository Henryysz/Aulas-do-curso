lista = {}
notas = []

nome = input('Nome do aluno: ').strip().title()
for num in range(1, 5):
    nota = float(input(f'Digite a {num}ª nota: '))
    notas.append(nota)

notas.sort()

lista['Nome'] = nome
lista['Notas'] = notas
lista['Maior nota'] = max(notas)
lista['Menor nota'] =  min(notas)
lista['Média'] = sum(notas) / len(notas)
lista['Situação'] = 'Aprovado' if lista['Média'] > 7 else 'Reprovado'

print()
print(f'O(A) aluno(a) {lista["Nome"]} obteve as seguintes notas: {lista["Notas"]} ')
print('-' * 60)
print(f'Sua maior nota foi {lista["Maior nota"]}, já sua menor nota foi {lista["Menor nota"]}')
print('-' * 60)
print(f'Sua média é {lista["Média"]}, ou seja, {lista["Situação"]}!') 
print('-' * 60)
