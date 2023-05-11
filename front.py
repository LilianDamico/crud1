import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("CRUD em Python com Tkinter")

# Labels
label_nome = ttk.Label(root, text="Nome:")
label_idade = ttk.Label(root, text="Idade:")
label_email = ttk.Label(root, text="E-mail:")

# Entradas de texto
entry_nome = ttk.Entry(root, width=30)
entry_idade = ttk.Entry(root, width=10)
entry_email = ttk.Entry(root, width=30)

# Botões
btn_inserir = ttk.Button(root, text="Inserir")
btn_atualizar = ttk.Button(root, text="Atualizar")
btn_excluir = ttk.Button(root, text="Excluir")
btn_listar = ttk.Button(root, text="Listar")

label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_idade.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

label_email.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_email.grid(row=2, column=1, padx=5, pady=5)

btn_inserir.grid(row=3, column=0, padx=5, pady=5)
btn_atualizar.grid(row=3, column=1, padx=5, pady=5)
btn_excluir.grid(row=3, column=2, padx=5, pady=5)
btn_listar.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
