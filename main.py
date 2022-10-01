import os
import platform
import sys
from time import sleep
from modulos.connection import conexao
from modulos.dmql import (
    listar_dados
)
from modulos.menu import(
    menu_principal
)

cnx = conexao()

cursor = cnx.cursor()

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

menu_principal()
opcao= int(input('Opção: '))
if opcao == 5:
    print('Encerrando o programa...')
    sleep(2)
    sys.exit('Programa encerrado')

print(listar_dados(cursor, colunas='LOGIN'))