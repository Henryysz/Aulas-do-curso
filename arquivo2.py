pessoas = [
           {
             'nome': 'Rafael',
             'idade': 46
           },
           {
             'nome': 'Gustavo',
             'idade': 25
           },
           {
             'nome': 'Willian',
             'idade': 22
           }
]

def menor_trinta(dict):
    if dict['idade'] < 30:
        return dict['nome']
    else:
        return ''
    
print(list(map(menor_trinta, pessoas)))