from take_and_analyze_a_picture_neural import tirar_e_analisar_foto_rede as tirar_e_analisar_foto
# from take_and_analyze_a_picture_cascate import tirar_e_analisar_foto_cascata as tirar_e_analisar_foto
from face_comparison import comparar_faces_funcionarios
from file_opening import abrir_arquivos

# Bloco destinado à captura, analise e comparação de rostos
image_path = tirar_e_analisar_foto('faces/analyzing', 'imagem_capturada.jpg')
cargo_do_analisado = comparar_faces_funcionarios(image_path)
print(f"Cargo do analisado: {cargo_do_analisado}")

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