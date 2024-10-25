import cv2
import os


def tirar_e_analisar_foto(save_path, image_name):
    print("Tirando foto..."
          "\nCertifique-se de que a câmera está funcionando corretamente."
          "\nDeixe o rosto bem centralizado.")

    # Verifica se a pasta existe, caso contrário, cria
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Carregar o classificador em cascata para detecção de rostos
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

    if face_cascade.empty():
        print("Erro ao carregar o classificador em cascata.")

    # Abrir a webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None

    # Captura uma imagem
    ret, frame = cap.read()

    # Verifica se a captura foi bem-sucedida
    if not ret:
        print("Não foi possível capturar a imagem.")
        cap.release()
        return None

    # Converter a imagem para escala de cinza e aplicar melhorias
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)  # Equalização do histograma na imagem em escala de cinza
    frame = cv2.GaussianBlur(frame, (5, 5), 0)  # Aplicar suavização na imagem original

    # Detectar rostos na imagem
    # scaleFactor: Um valor mais baixo faz a detecção ser mais sensível a rostos de tamanhos diferentes. Tente
    # diminuir de 1.1 para algo como 1.05.
    # minNeighbors: Um valor menor aumenta a chance de detecção, mas pode gerar
    # mais falsos positivos. Tente reduzir de 5 para 3.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(30, 30))  # PARAMETROS IMPORTANTES

    image_path = None  # Initialize image_path

    if len(faces) == 0:
        print("Nenhum rosto detectado.")
    else:
        print(f"{len(faces)} rosto(s) detectado(s).")
        # Desenhar retângulos ao redor dos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar a imagem com os rostos detectados
        cv2.imshow('faces Detectados', frame)

        # Salvar a imagem capturada na pasta especificada
        image_path = os.path.join(save_path, image_name)
        cv2.imwrite(image_path, frame)
        print(f"Imagem salva em: {image_path}")

    # Libera a webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()

    return image_path


tirar_e_analisar_foto('faces/analyzing', 'imagem_capturada.jpg')
