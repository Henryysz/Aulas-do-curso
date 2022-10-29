nomes = ['Gabriel',
         'Allan',
         'Camila',
         'Gisele',
         'Henry',
         'Rafael',
         'Alvacy',
         'Pedro',
         'Galego',
         'Renan',
         'Diego',
         'Kaique',
         'Silas',
         'João',
         'Eduardo'
         ]

#nomes.sort(key=lambda letras: letras[-1], reverse=True)
#print(nomes)

#print(list(map(lambda letra: letra.upper(), nomes)))

#def dividir_numero(numeros):
    #return numeros / 2

#def dobrar_numero(numeros):
 #   return numeros * 2


#print(list(map(dividir_numero, range(1, 21))))

#print(list(map(dobrar_numero, range(1, 21))))

print(list(filter(lambda Letra: Letra.endswith('o'), nomes)))