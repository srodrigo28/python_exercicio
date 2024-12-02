
valor = ""
contador = 1

while valor.lower() != "sair":
    valor = input("Informe algo ou sair: ")
    print(f"Você digitou {contador}. {valor}")
    contador += 1
print("Fim!")