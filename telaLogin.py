import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def login():
    cpf = input_cpf.get()
    senha = input_senha.get()
    
    if cpf == "123.456.789-00" and senha == "2344":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        print("CPF:", cpf)
        print("Senha digitada:", senha)
        print("Login Realizado!")
    else:
        messagebox.showerror("Erro", "CPF ou senha incorretos.")
        print("Falha no login - CPF:", cpf)

# Janela principal
app = tk.Tk()
app.title("Login - Sistema")
app.geometry("450x400")
app.configure(bg="#f0f2f5")
app.eval('tk::PlaceWindow . center')

# Frame principal
main_frame = tk.Frame(app, bg="#f0f2f5")
main_frame.pack(expand=True, fill="both")

# LOGO (texto com emoji)
logo_img = PhotoImage(file="/home/escola/Downloads/LOGO sem fundo.png")  # substitua pelo nome do arquivo
logo_img = logo_img.subsample(2, 2) 
logo_label = tk.Label(app, image=logo_img, bg="#f0f2f5")
logo_label.pack(pady=(10, 10))

# Título
titulo = tk.Label(main_frame, text="Acesso ao Sistema", font=("Segoe UI", 18, "bold"),
                  bg="#f0f2f5", fg="#2c3e50")
titulo.pack(pady=(0, 25))

# Frame para os campos
form_frame = tk.Frame(main_frame, bg="#f0f2f5")
form_frame.pack(expand=True)

# Campo CPF
label_cpf = tk.Label(form_frame, text="CPF (com pontos e traço):", font=("Segoe UI", 11),
                     bg="#f0f2f5", fg="#34495e", anchor="w")
label_cpf.pack(fill="x", pady=(0, 5))

input_cpf = tk.Entry(form_frame, font=("Segoe UI", 11), relief="solid", bd=1,
                     highlightthickness=1, highlightcolor="#3498db")
input_cpf.pack(fill="x", ipady=6, pady=(0, 15))

# Campo Senha
label_senha = tk.Label(form_frame, text="Senha:", font=("Segoe UI", 11),
                       bg="#f0f2f5", fg="#34495e", anchor="w")
label_senha.pack(fill="x", pady=(0, 5))

input_senha = tk.Entry(form_frame, font=("Segoe UI", 11), show="*",
                       relief="solid", bd=1, highlightthickness=1, highlightcolor="#3498db")
input_senha.pack(fill="x", ipady=6, pady=(0, 25))

# Botão
def on_enter(e):
    btn_enviar.config(bg="#2980b9")

def on_leave(e):
    btn_enviar.config(bg="#3498db")

btn_enviar = tk.Button(form_frame, text="Entrar", command=login,
                       font=("Segoe UI", 11, "bold"), bg="#3498db", fg="white",
                       relief="flat", padx=20, pady=8, cursor="hand2")
btn_enviar.pack(pady=10)
btn_enviar.bind("<Enter>", on_enter)
btn_enviar.bind("<Leave>", on_leave)

app.bind('<Return>', lambda event: login())

app.mainloop()