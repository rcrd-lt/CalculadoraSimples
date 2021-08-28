#função de operação
def operacao():
    if op == "+":
        resultado = (num1 + num2)
    if op == "-":
        resultado = (num1 - num2)
    if op == "*":
        resultado = (num1 * num2)
    if op == "/":
        resultado = (num1 / num2)
    if op == "+" or op == "-" or op == "*" or op == "/":
        print("O resultado é: ", str(resultado))
    else:
        print("Operação não é válida")

#variáveis de operação
num1 = float(input("Digite o primeiro número: \n"))
op = input("Operação desejada: [+] Soma - [-] Subtração - [*] Multiplicação - [/] Divisão \n")
num2 = float(input("Digite o segundo número: \n"))

#executa:
operacao()


