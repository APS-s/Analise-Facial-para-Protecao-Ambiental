import cv2


def analisa_rosto(image_path):
    # Carregar o classificador em cascata para detecção de rostos
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

    # Carregar a imagem
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        print("Nenhum rosto detectado.")
        return
    else:
        # Desenhar retângulos ao redor dos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar a imagem com os rostos detectados
        # cv2.imshow('faces Detectados', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


# Exemplo de uso
analisa_rosto('faces/analyzing/imagem_capturada.jpg')
