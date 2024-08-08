import tkinter as tk
from tkinter import messagebox

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def calcular():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operacao = operacao_var.get()
        
        if operacao == "Adição":
            resultado = adicionar(num1, num2)
        elif operacao == "Subtração":
            resultado = subtrair(num1, num2)
        elif operacao == "Multiplicação":
            resultado = multiplicar(num1, num2)
        elif operacao == "Divisão":
            resultado = dividir(num1, num2)
        
        result_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("400x300")

label1 = tk.Label(root, text="Digite o primeiro número:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Digite o segundo número:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

operacao_var = tk.StringVar(root)
operacao_var.set("Adição")

label3 = tk.Label(root, text="Selecione a operação:")
label3.pack()

operacao_menu = tk.OptionMenu(root, operacao_var, "Adição", "Subtração", "Multiplicação", "Divisão")
operacao_menu.pack()

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.pack()

result_label = tk.Label(root, text="Resultado: ")
result_label.pack()

root.mainloop()
