def somar(num1, num2):
    return (num1 + num2)


def subtrair(num1, num2):
    return (num1 - num2)


def dividir(num1, num2):
    return (num1 / num2)


def multiplicar(num1, num2):
    return (num1 * num2)


def potenciacao(num1, num2):
    return (num1 ** num2)


def resto(num1, num2):
    return (num1 % num2)


def raiz_quadrada(num1, num2):
    return (num1 * num1), (num2 * num2)


while True:
    num1 = int(input("Qual o primeiro numero? "))
    num2 = int(input("Qual o segundo numero? "))
    operacao = input("""Qual operação matematica quer fazer?
    +  -> Soma
    -  -> Subtração
    *  -> Multiplicação
    /  -> Divisão
    ** -> Potenciação
    %  -> Resto da Divisão
    x  -> Raiz quadrada
    : """)

    if operacao == "+":
        print("O Resultado é: ", somar(num1, num2))
    elif operacao == "-":
        print("O Resultado é: ", subtrair(num1, num2))
    elif operacao == "*":
        print("O Resultado é: ", multiplicar(num1, num2))
    elif operacao == "/":
        print("O Resultado é: ", dividir(num1, num2))
    elif operacao == "**":
        print("O Resultado é: ", potenciacao(num1, num2))
    elif operacao == "%":
        print("O Resultado é: ", resto(num1, num2))
    elif operacao == "x":
        print("A Raiz quadrada dos dois numeros: ", raiz_quadrada(num1, num2))

    cont = input("Quer fazer de novo? ")
    cont = cont.lower()
    if cont == "sim" or cont == "ss" or cont == "s":
        pass
    else:
        break
