import cv2
import numpy as np
import os
from database_connection import conexao_a_database


def compare_faces(image_path):
    # Conectar ao banco de dados usando a função database_connection
    conn = conexao_a_database()
    if conn is None:
        print("Erro ao conectar ao banco de dados.")
        return None

    cursor = conn.cursor()

    # Carregar a imagem analisada
    analyzed_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Obter todos os endereços de rostos e cargos do banco de dados
    cursor.execute("SELECT rosto, cargo FROM pessoasautorizadas")
    rows = cursor.fetchall()

    cargo_do_analisado = None

    for (db_face_path, db_cargo) in rows:
        # Ajustar o caminho da imagem
        
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

        # Comparar as imagens (usando, por exemplo, a diferença absoluta)
        if np.array_equal(analyzed_image, db_face_image):
            cargo_do_analisado = db_cargo
            break

    cursor.close()
    conn.close()

    return cargo_do_analisado


# Exemplo de uso
image_path = 'Rostos/Em analise/imagem_capturada.jpg'
cargo_do_analisado = compare_faces(image_path)
print(f"Cargo do analisado: {cargo_do_analisado}")
