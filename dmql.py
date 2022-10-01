
def listar_dados(cursor, colunas='*'):
    query = f'SELECT {colunas} FROM USERS'
    cursor.execute(query)
    if colunas != '*':
        return [valor[0] for valor in cursor.fetchall()]
    return cursor.fetchall()

def inserir_dados():
    pass

def atualizar_dados():
    pass

def apagar_dados():
    pass

if __name__ == '__main__':
    print(__doc__)
