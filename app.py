
# IMPORTANDO OS MODULOS DO TKINTER 
import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox

COR_FUNDO = "#FFFFFF"
COR_TEXTO = "#333333"
COR_PRIMARIA = "#007BFF"
COR_SECUNDARIA = "#DC3545"
COR_TEXTO_BOTAO = "#FFFFFF"
FONTE_TITULO = ("Segoe UI", 24, "bold")
FONTE_NORMAL = ("Segoe UI", 12)
FONTE_LISTA = ("Segoe UI", 11)

# RECEBENDO INFORMAÇÕES DO USUÁRIO E ADICIONANDO A TAREFA NA LISTA
def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, digite uma tarefa válida.")

# DELETANDO A TAREFA SELECIONADA NA LISTA
def deletar_tarefa():
    try:
        indices_selecionados = lista_tarefas.curselection()
        if not indices_selecionados:
            raise IndexError 
            
        indice_selecionado = indices_selecionados[0]
        lista_tarefas.delete(indice_selecionado)
    except IndexError:
        messagebox.showwarning("Atenção", "Por favor, selecione uma tarefa para deletar.")

# CONFIGURAÇÃO DA JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Gerenciador de Tarefas Moderno")
janela.geometry("450x550") 
janela.configure(bg=COR_FUNDO) 

# INVOCANDO O ESTILO DO TTK PARA PERSONALIZAR OS WIDGETS
style = ttk.Style()

style.theme_use('clam')

style.configure("TFrame", background=COR_FUNDO)

style.configure("TLabel", background=COR_FUNDO, foreground=COR_TEXTO, font=FONTE_NORMAL)

style.configure("Titulo.TLabel", font=FONTE_TITULO, padding=(0, 0, 0, 20))

# ESTILIZAÇÃO DO ENTRY
style.configure("TEntry",
                fieldbackground=COR_FUNDO,
                foreground=COR_TEXTO,
                font=FONTE_NORMAL,
                bordercolor="#CED4DA", 
                lightcolor="#CED4DA",
                darkcolor="#CED4DA",
                padding=(10, 8)) 

# ESTILIZAÇÃO BOTÃO PRIMÁRIO
style.configure("Primario.TButton",
                font=("Segoe UI", 11, "bold"),
                background=COR_PRIMARIA,
                foreground=COR_TEXTO_BOTAO,
                padding=10,
                borderwidth=0,
                relief="flat")
style.map("Primario.TButton",
          background=[('active', '#0069D9')],
          foreground=[('active', COR_TEXTO_BOTAO)])

# ESTILIZAÇÃO BOTÃO SECUNDÁRIO
style.configure("Secundario.TButton",
                font=("Segoe UI", 11, "bold"),
                background=COR_SECUNDARIA,
                foreground=COR_TEXTO_BOTAO,
                padding=10,
                borderwidth=0,
                relief="flat")
style.map("Secundario.TButton",
          background=[('active', '#C82333')], 
          foreground=[('active', COR_TEXTO_BOTAO)])

# CRIANDO O PAINEL PRINCIPAL PARA ORGANIZAR OS WIDGETS
painel_principal = ttk.Frame(janela, padding=30, style="TFrame")
painel_principal.pack(fill="both", expand=True)

# TÍTULO
label_titulo = ttk.Label(painel_principal, text="Minhas Tarefas do Dia", style="Titulo.TLabel")
label_titulo.pack()

# ENTRADA DE TAREFA E BOTÃO DE ADICIONAR
frame_entrada = ttk.Frame(painel_principal, style="TFrame")
frame_entrada.pack(fill="x", pady=10)

entrada_tarefa = ttk.Entry(frame_entrada, style="TEntry")
entrada_tarefa.pack(side="left", fill="x", expand=True, padx=(0, 10))

# PERMITIR ADICIONAR TAREFAS USANDO ENTER
entrada_tarefa.bind('<Return>', lambda event: adicionar_tarefa())

botao_adicionar = ttk.Button(frame_entrada, text="Adicionar", command=adicionar_tarefa, style="Primario.TButton")
botao_adicionar.pack(side="right")

# LISTA DE TAREFAS COM SCROLLBAR
frame_lista = ttk.Frame(painel_principal, style="TFrame")
frame_lista.pack(fill="both", expand=True, pady=15)

# ESILIZAÇÃO LISTBOX
lista_tarefas = tk.Listbox(frame_lista,
                           font=FONTE_LISTA,
                           selectbackground=COR_PRIMARIA,
                           selectforeground=COR_TEXTO_BOTAO,
                           selectmode="single",
                           borderwidth=1,
                           relief="solid", 
                           highlightthickness=1,
                           highlightbackground="#CED4DA") 
lista_tarefas.pack(side="left", fill="both", expand=True)

# ESTILIZAÇÃO DA SCROLLBAR
barra_rolagem = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_tarefas.yview)
barra_rolagem.pack(side="right", fill="y")
lista_tarefas.config(yscrollcommand=barra_rolagem.set)

# BOTTÃO DELETE
botao_deletar = ttk.Button(painel_principal, text="Deletar Tarefa Selecionada", command=deletar_tarefa, style="Secundario.TButton")
botao_deletar.pack(fill="x", pady=(20, 0))

# INICIAR APP
janela.mainloop()