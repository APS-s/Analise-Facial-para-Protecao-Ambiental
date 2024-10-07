import mysql.connector


def conexao_a_database():
    # Conectar ao banco de dados
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pateta',
            database='analisefacial'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None
