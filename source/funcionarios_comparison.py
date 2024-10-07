import cv2
import numpy as np
import os
from database_connection import conexao_a_database


# TODO: Aumentar a precisão do reconhecimento de rostos
# TODO: Modificar o nome do Script e do Metodo para então adicionar o
#  metodo comparar_faces_funcionarios() e comparar_faces_perigosos()
def compare_faces(image_path):
    # Conectar ao banco de dados usando a função database_connection
    conn = conexao_a_database()
    if conn is None:
        print("Erro ao conectar ao banco de dados.")
        return None

    cursor = conn.cursor()

    # Carregar a imagem analisada
    analyzed_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if analyzed_image is None:
        print(f"Erro ao carregar a imagem analisada: {image_path}")
        return None

    # Inicializar o reconhecedor de rostos LBPH
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Obter todos os endereços de rostos e cargos do banco de dados
    cursor.execute("SELECT rosto, cargo FROM pessoasautorizadas")
    rows = cursor.fetchall()

    cargo_do_analisado = None

    for (db_face_path, db_cargo) in rows:
        print(f"Tentando carregar a imagem do caminho: {db_face_path}")

        # Verificar se o arquivo existe
        if not os.path.exists(db_face_path):
            print(f"Arquivo não encontrado: {db_face_path}")
            continue

        # Carregar a imagem do banco de dados a partir do endereço de arquivo
        db_face_image = cv2.imread(db_face_path, cv2.IMREAD_GRAYSCALE)
        if db_face_image is None:
            print(f"Erro ao carregar a imagem: {db_face_path}")
            continue

        # Treinar o reconhecedor com a imagem do banco de dados
        recognizer.train([db_face_image], np.array([0]))

        # Realizar a previsão na imagem analisada
        label, confidence = recognizer.predict(analyzed_image)
        print(f"Confiança: {confidence}")

        # Definir um limiar de confiança para considerar uma correspondência
        if confidence < 50:  # Ajuste o valor conforme necessário
            cargo_do_analisado = db_cargo
            break

    cursor.close()
    conn.close()

    return cargo_do_analisado


# Exemplo de uso
image_path = 'Rostos/Em analise/imagem_capturada.jpg'
cargo_do_analisado = compare_faces(image_path)
print(f"Cargo do analisado: {cargo_do_analisado}")
