import tkinter as tk 
from tkinter import messagebox

def cadastrar():
    print("texto")

titulo = tk.label(aapp, text="Cadastro dos clientes", font=)

app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")

label_agencia = tk.Label(app, text ="Agência:")
label_agencia.pack(pady=5)
input_agencia = tk.Entry(app)
input_agencia.pack()

label_titular = tk.Label(app, text ="Titular:")
label_titular.pack(pady=4)
input_titular = tk.Entry(app)
input_titular.pack()

label_cpf = tk.Label(app, text ="CPF:")
label_cpf.pack(pady=4)
input_cpf = tk.Entry(app)
input_cpf.pack()

btn_enviar = tk.Button(app, text="Enviar", command=cadastrar)
btn_enviar.pack()

app.mainloop()