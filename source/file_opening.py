import os


def abrir_arquivos(valor):
    file_path = os.path.abspath(f'confidencial_documents/Doc{valor}.pdf')
    # print(f"Resolved file path: {file_path}")
    if os.path.exists(file_path):
        os.startfile(file_path)
        print(f"Abrindo Arquivo {valor}")
    else:
        print(f"Arquivo {file_path} não encontrado. Verifique se o caminho está correto e se o arquivo existe.")
