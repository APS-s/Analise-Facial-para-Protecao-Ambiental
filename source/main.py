from file_opening import abrir_arquivos
from database_connection import conexao_a_database
from source.funcionarios_comparison import cargo_do_analisado
from take_a_picture import tirar_foto
from picture_analyze import analisa_rosto
from funcionarios_comparison import compare_faces

# Bloco destinado a captura, analise e comparação de rostos
tirar_foto()
analisa_rosto('Rostos/Em analise/imagem_capturada.jpg')
cargo_do_analisado = compare_faces('Rostos/Em analise/imagem_capturada.jpg')

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
