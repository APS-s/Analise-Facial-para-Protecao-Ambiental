import cv2
import os


def tirar_e_analisar_foto(save_path, image_name):
    print("Tirando foto..."
          "\nCertifique-se de que a câmera está funcionando corretamente."
          "\nDeixe o rosto bem centralizado.")

    # Verifica se a pasta existe, caso contrário, cria
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Abrir a webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None

    print("Após enquadramento, pressione a tecla ESQ")
    while True:
        ret_val, img = cap.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit

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
    gray = cv2.equalizeHist(gray)

    # Aplicar desfoque para reduzir ruído
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    image_path = None

    # Salvar a imagem capturada na pasta especificada
    image_path = os.path.join(save_path, image_name)
    cv2.imwrite(image_path, gray)
    print(f"Imagem salva em: {image_path}")

    # Libera a webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()

    return image_path


# tirar_e_analisar_foto('faces/analyzing', 'imagem_capturada.jpg')
