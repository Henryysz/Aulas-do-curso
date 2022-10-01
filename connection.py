import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv('./modulos/env')

def conexao():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('HOST'),
            port=os.getenv('PORT'),
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            db=os.getenv('DB')
    )
    except Exception as err:
        raise err('Não foi possível conectar ao BD')
    else:
        print('[ MySQL ] Conexão bem sucedida')
        return conn
    
if __name__ == '__main__':
    print(__doc__)

