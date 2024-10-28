import dlib
import cv2
import numpy as np
import os
from database_connection import conexao_a_database


def comparar_faces_funcionarios(image_path):
    min_distance = 0.5

    # Conectar ao banco de dados usando a função database_connection
    conn = conexao_a_database()
    if conn is None:
        print("Erro ao conectar ao banco de dados.")
        return None

    cursor = conn.cursor()

    # Carregar a imagem analisada
    analyzed_image = cv2.imread(image_path)
    if analyzed_image is None:
        print(f"Erro ao carregar a imagem analisada: {image_path}")
        return None

    # Inicializar o detector de rostos e o reconhecedor de rostos
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
    facerec = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")

    # Detectar rostos na imagem analisada
    dets = detector(analyzed_image, 1)
    if len(dets) == 0:
        print("Nenhum rosto detectado na imagem analisada.")
        return None

    # Obter a descrição do rosto analisado
    shape = sp(analyzed_image, dets[0])
    analyzed_face_descriptor = facerec.compute_face_descriptor(analyzed_image, shape)

    # Obter todos os endereços de rostos e cargos do banco de dados
    cursor.execute("SELECT rosto, cargo FROM pessoasautorizadas")
    rows = cursor.fetchall()

    cargo_do_analisado = "Nenhum"
    # min_distance = float("inf")

    for (db_face_path, db_cargo) in rows:
        print(f"Tentando carregar a imagem do caminho: {db_face_path}")

        # Verificar se o arquivo existe
        if not os.path.exists(db_face_path):
            print(f"Arquivo não encontrado: {db_face_path}")
            continue

        print(f"Carregando a imagem do caminho: {db_face_path}")

        # Carregar a imagem do banco de dados a partir do endereço de arquivo
        db_face_image = cv2.imread(db_face_path)
        if db_face_image is None:
            print(f"Erro ao carregar a imagem: {db_face_path}")
            continue

        # Detectar rostos na imagem do banco de dados
        db_dets = detector(db_face_image, 1)
        if len(db_dets) == 0:
            print(f"Nenhum rosto detectado na imagem: {db_face_path}")
            continue

        # Obter a descrição do rosto do banco de dados
        db_shape = sp(db_face_image, db_dets[0])
        db_face_descriptor = facerec.compute_face_descriptor(db_face_image, db_shape)

        # Calcular a distância entre os descritores de rosto
        distance = np.linalg.norm(np.array(db_face_descriptor) - np.array(analyzed_face_descriptor))
        print(f"Distância: {distance}")

        # Definir um limiar de distância para considerar uma correspondência
        if distance <= min_distance:
            # min_distance = distance
            cargo_do_analisado = db_cargo

    cursor.close()
    conn.close()

    return cargo_do_analisado


# comparar_faces_funcionarios('faces/analyzing/imagem_capturada.jpg')
