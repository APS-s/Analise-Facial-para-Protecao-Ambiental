import cv2
import os


def tirar_e_analisar_foto_cascata(save_path, image_name):
    image_path = None
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
        return None

    # Abre a webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None

    print("Pressione a tecla 'ESC' para salvar a imagem e sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não foi possível capturar a imagem.")
            break

        # Converter a imagem para escala de cinza e aplicar melhorias
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)  # Equalização do histograma na imagem em escala de cinza
        frame = cv2.GaussianBlur(frame, (5, 5), 0)  # Aplicar suavização na imagem original

        # Detectar rostos na imagem
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(30, 30))

        num_faces = len(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar a imagem com os rostos detectados
        cv2.imshow('Faces Detectadas', frame)

        # Verificar se a tecla 'ESC' foi pressionada para salvar a imagem e sair
        if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for ESC
            image_path = os.path.join(save_path, image_name)
            cv2.imwrite(image_path, frame)
            print(f"Imagem salva em: {image_path}")
            print(f"Número de rostos detectados: {num_faces}")
            break

    # Libera a webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()

    return image_path
