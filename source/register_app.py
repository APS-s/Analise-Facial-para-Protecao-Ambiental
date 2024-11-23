import tkinter as tk
from tkinter import messagebox
from take_and_analyze_a_picture_neural import tirar_e_analisar_foto_rede as tirar_e_analisar_foto
# from take_and_analyze_a_picture_cascate import tirar_e_analisar_foto_cascata as tirar_e_analisar_foto
from database_connection import conexao_a_database

global image_path
image_path = None


# Função para salvar os dados no banco de dados
def salvar_dados(nome, cargo, image_path_def):
    try:
        if not nome:
            raise ValueError("Nome não foi preenchido.")
        if not cargo:
            raise ValueError("Cargo não foi selecionado.")
        if not image_path_def:
            raise ValueError("Foto não foi tirada.")

        with conexao_a_database() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pessoasautorizadas (nome_completo, cargo, rosto) VALUES (%s, %s, %s)
            ''', (nome, cargo, image_path_def))
            conn.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
        return True
    except ValueError as ve:
        messagebox.showwarning("Aviso", str(ve))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")
    return False


def tirar_foto_wrapper():
    try:
        with conexao_a_database() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM pessoasautorizadas")
            max_id = cursor.fetchone()[0]
            next_id = 1 if max_id is None else max_id + 1

            image_path_local = 'faces/employees/'
            image_name = f'face_{next_id}.jpg'
            return tirar_e_analisar_foto(image_path_local, image_name)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao tirar a foto: {e}")
        return None


def criar_ui():
    root = tk.Tk()
    root.title("Registro de Funcionários")

    tk.Label(root, text="Nome Completo").grid(row=0, column=0, padx=10, pady=10)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Cargo").grid(row=1, column=0, padx=10, pady=10)
    cargo_var = tk.StringVar()
    cargos = ["Ministro", "Diretor de Pesquisa", "Coordenador de Segurança", "Assessor de Comunicação",
              "Analista de Dados", "Estagiário"]

    for idx, cargo in enumerate(cargos):
        tk.Radiobutton(root, text=cargo, variable=cargo_var, value=cargo).grid(row=2 + idx, column=1, padx=10, pady=2,
                                                                               sticky=tk.W)

    def on_tirar_foto():
        global image_path
        image_path = tirar_foto_wrapper()

    def on_salvar_dados():
        global image_path
        nome = entry_nome.get()
        cargo2 = cargo_var.get()
        if not image_path:
            messagebox.showwarning("Aviso", "Por favor, tire a foto antes de salvar.")
            return
        if salvar_dados(nome, cargo2, image_path):
            image_path = None  # Reseta o image_path para que o usuario possa continuar adicionando funcionarios

    btn_foto = tk.Button(root, text="Tirar Foto", command=on_tirar_foto)
    btn_foto.grid(row=8, column=1, padx=10, pady=10)

    btn_salvar = tk.Button(root, text="Salvar", command=on_salvar_dados)
    btn_salvar.grid(row=9, column=1, padx=10, pady=10)

    root.mainloop()


# Executar a UI
criar_ui()
