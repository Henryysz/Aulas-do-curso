from distutils.log import info
from produto import Produto

produtos = []

while True:
    p1 = Produto(
        input('Nome: ').title(),
        float(input('Preço: [R$]')),
        input('Categoria: '),
        input('Descrição: ')
    )
    
    produtos.append(p1)

    if input('Continuar? ') in 'nN':
        break
    
for prod in produtos:
    print('-' * 20)
    print(
        prod.nome,
        prod.preco,
        prod.categoria,
        prod.descricao,
        sep='\n'   
    )
    