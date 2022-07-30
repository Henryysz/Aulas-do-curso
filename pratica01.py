dados = {}

nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
idade = int(input('Digite sua idade: '))
email = input('Digite seu email: ').strip().lower()

dados['nome'], dados['sobrenome'], dados['idade'], dados['email'] = nome, sobrenome, idade, email

for indice, dado in enumerate(dados.items(), start=1):


