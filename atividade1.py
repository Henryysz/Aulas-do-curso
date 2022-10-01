import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv('./.env')

try:
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        passwd=os.getenv('PASSWD'),
        db=os.getenv('DB')
    )
except Exception as err:
    raise err('Deu ruim')
else:
    #print(conn.is_connected())
    cur = conn.cursor()

query = 'SELECT LOGIN FROM USERS'
cur.execute(query)
users = [ user[0] for user in cur.fetchall()]
print(users)

print('Qual registro deseja atualizar?')
for pos, login in enumerate(users, start=1):
    print(pos, login, sep= ' : ')
opcao = int(input('Opção: '))

query = f'DELETE FROM USERS WHERE LOGIN="{users[opcao -1]}"'
cur.execute(query)
conn.commit()

# nome = input('Novo nome: ').title()
# query = f'UPDATE USERS SET FULL_NAME="{nome}" WHERE login="{users[opcao - 1]}"'
# cur.execute(query)
# conn.commit()

# login = input('Login: ').lower()

# while login in users:
#     print(f'Login {login} já existe')
#     login = input('Login: ').lower()
    
# if login not in users:
#     nome = input('Nome: ').title()
#     query = f'INSERT INTO USERS VALUES ("{login}", "{nome}")'
#     cur.execute(query)
#     conn.commit()



# query = 'SELECT * FROM USERS'
# cur.execute(query)
# retorno = cur.fetchall()

# for login, nome in retorno:
#     print(login, nome, sep= ' ----- ')



