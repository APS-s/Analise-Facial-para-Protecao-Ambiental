from take_a_picture import tirar_foto
from picture_analyze import analisa_rosto
from database_connection import conexao_a_database
import face_comparison
from file_opening import abrir_arquivos


# Bloco destinado a captura, analise e comparação de rostos
# Não é necessário implementar os métodos: tirar_foto, analisa_rosto e conexao_a_database,
# pois já foram implementados em seus respectivos scripts e são executados quando
# chamados.
cargo_do_analisado = face_comparison.cargo_do_analisado

# Definindo os níveis de acesso
nivel_acesso1 = ['Coordenador de Segurança', 'Assessor de Comunicação', 'Analista de Dados']
nivel_acesso2 = ['Diretor de Pesquisa']
nivel_acesso3 = ['Ministro']

# Verificando se o cargo possui acesso a algum documento
if cargo_do_analisado in nivel_acesso1:
    abrir_arquivos(1)
elif cargo_do_analisado in nivel_acesso2:
    abrir_arquivos(2)
elif cargo_do_analisado in nivel_acesso3:
    abrir_arquivos(3)
else:
    print("Acesso negado.")