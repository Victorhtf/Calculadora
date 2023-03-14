import tkinter as tk

# Definindo as funções das operações básicas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

# Definindo a função que será chamada quando o botão calcular for clicado
def calcular():
    # Recebendo os valores digitados pelo usuário
    operacao = operacao_entry.get()
    numero1 = int(numero1_entry.get())
    numero2 = int(numero2_entry.get())

    # Verificando a escolha do usuário e chamando a função correspondente
    if operacao == '1':
        resultado = adicao(numero1, numero2)
    elif operacao == '2':
        resultado = subtracao(numero1, numero2)
    elif operacao == '3':
        resultado = multiplicacao(numero1, numero2)
    elif operacao == '4':
        resultado = divisao(numero1, numero2)
    else:
        resultado = "Opção inválida"

    # Exibindo o resultado na label
    resultado_label.config(text="O resultado é: " + str(resultado))

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Criando os widgets da interface gráfica
operacao_label = tk.Label(root, text="Selecione a operação: \n1 - Adição \n2- Subtração \n3 - Multiplicação \n4 - Divisão")
operacao_label.pack()

operacao_entry = tk.Entry(root, width=5)
operacao_entry.pack()

numero1_label = tk.Label(root, text="Digite o primeiro número:")
numero1_label.pack()

numero1_entry = tk.Entry(root, width=10)
numero1_entry.pack()

numero2_label = tk.Label(root, text="Digite o segundo número:")
numero2_label.pack()

numero2_entry = tk.Entry(root, width=10)
numero2_entry.pack()

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Iniciando a execução da janela principal
root.mainloop()
