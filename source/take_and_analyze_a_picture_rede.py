import cv2
import os
import numpy as np


# Com desfoque e escala de cinza, foram obtidos os maiores valores
def tirar_e_analisar_foto_rede(save_path, image_name):
    image_path = None
    print("Tirando foto..."
          "\nCertifique-se de que a câmera está funcionando corretamente."
          "\nDeixe o rosto bem centralizado.")

    # Verifica se a pasta existe, caso contrário, cria
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Carregar o modelo de rede neural
    prototxt_path = 'models/deploy.prototxt'
    model_path = 'models/res10_300x300_ssd_iter_140000.caffemodel'
    face_net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    # Abrir a webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None

    while True:
        ret_val, img = cap.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit

    # Captura uma imagem
    ret, frame = cap.read()

    # Verifica se a captura foi bem-sucedida
    if not ret:
        print("Não foi possível capturar a imagem.")
        cap.release()
        return None

    # Converter a imagem para escala de cinza e equalizar o histograma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Aplicar desfoque para reduzir ruído
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Converter a imagem para blob para a rede neural
    blob_dimension_x, blob_dimension_y = 400, 400
    blob = cv2.dnn.blobFromImage(frame, 1.0, (blob_dimension_x, blob_dimension_y), (104.0, 177.0, 123.0))

    # Passar o blob pela rede
    face_net.setInput(blob)
    detections = face_net.forward()

    # Loop sobre as detecções
    (h, w) = frame.shape[:2]
    faces_detected = 0
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.7:
            # Obter coordenadas do rosto
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Desenhar um retângulo ao redor do rosto detectado
            cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
            faces_detected += 1
    if faces_detected == 0:
        print("Nenhum rosto detectado.")
    else:
        print(f"{faces_detected} rosto(s) detectado(s).")

        # Mostrar a imagem com os rostos detectados
        cv2.imshow('Faces Detectadas', frame)

        # Salvar a imagem capturada na pasta especificada
        image_path = os.path.join(save_path, image_name)
        cv2.imwrite(image_path, gray)
        print(f"Imagem salva em: {image_path}")

    # Libera a webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()

    return image_path


tirar_e_analisar_foto_rede('faces/analyzing', 'imagem_capturada.jpg')
