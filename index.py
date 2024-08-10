import tkinter as tk
from tkinter import messagebox
#logica do programa
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
    global operacao
    global num1
    global num2
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
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

def botaoAdic():
    global operacao
    operacao = "Adição"

def botaoSub():
    global operacao
    operacao = "Subtração"

def botaoMul():
    global operacao
    operacao = "Multiplicação"

def botaoDiv():
    global operacao
    operacao = "Divisão"

def inserir_numero(numero):
    if entry1.focus_get() == entry1:
        entry1.insert(tk.END, str(numero))
    elif entry2.focus_get() == entry2:
        entry2.insert(tk.END, str(numero))
                      
#inicio da GUI
calculadora = tk.Tk()
calculadora.title("Calculadora Básica")
calculadora.geometry("600x600")


valor = tk.StringVar()
valor.set("0")


label1 = tk.Label(calculadora, text="Digite o primeiro número:")
label1.pack()

entry1 = tk.Entry(calculadora)
entry1.pack()

label2 = tk.Label(calculadora, text="Digite o segundo número:")
label2.pack()

entry2 = tk.Entry(calculadora)
entry2.pack()

frame_botoes = tk.Frame(calculadora)
frame_botoes.pack()

numeros = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('0', 3, 1)
]

for (numero, linha, coluna) in numeros: #botoes dos numeros
    botao = tk.Button( frame_botoes, text=numero, command=lambda t=numero: inserir_numero(t))
    botao.grid(row=linha, column=coluna)


operacaoAdi = tk.Button(calculadora, text="+", command=botaoAdic)
operacaoAdi.pack()

operacaoSub = tk.Button(calculadora, text="-", command=botaoSub)
operacaoSub.pack()

operacaoMul = tk.Button(calculadora, text="*", command=botaoMul)
operacaoMul.pack()

operacaoDiv = tk.Button(calculadora, text="/", command=botaoDiv)
operacaoDiv.pack()

calcular_button = tk.Button(calculadora, text="=", command=calcular)
calcular_button.pack()

result_label = tk.Label(calculadora, text="Resultado: ")
result_label.pack()

calculadora.mainloop()
