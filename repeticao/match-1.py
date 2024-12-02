n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
operation = input("Informe a operação: [ + - * /] ")

match operation:
    case "+":
        result = n1 + n2
        print(result)
    case "-":
        result = n1 - n2
        print(result)
    case "*" | "x":
        result = n1 * n2
        print(result)
    case "/":
        result = n1 / n2
        print(result)
    case _:
        print("Operação não encontrada ")