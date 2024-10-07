from file_opening import abrir_arquivos
from database_connection import conexao_a_database

# Analise Facial


# Conectando ao banco de dados
conn = database_connection()

if not conn:
    print("Erro ao conectar ao banco de dados.")

# Criando um cursor
cursor = conn.cursor()

# Definindo os níveis de acesso
nivel_acesso1 = ['Coordenador de Segurança', 'Assessor de Comunicação', 'Analista de Dados']
nivel_acesso2 = ['Diretor de Pesquisa']
nivel_acesso3 = ['Ministro']

# Executar uma consulta para obter o cargo do funcionário
cursor.execute("SELECT cargo FROM PessoasAutorizadas WHERE id = 1")  # Troque 1 pelo ID desejado
resultado = cursor.fetchone()

if resultado:
    cargo_funcionario = resultado[0]  # Pega o cargo do funcionário

    # Verificando se o cargo está na lista nivel_acesso1
    if cargo_funcionario in nivel_acesso1:
        abrir_arquivos(1)
    elif cargo_funcionario in nivel_acesso2:
        abrir_arquivos(2)
    elif cargo_funcionario in nivel_acesso3:
        abrir_arquivos(3)

# Fechar o cursor e a conexão
cursor.close()
conn.close()
