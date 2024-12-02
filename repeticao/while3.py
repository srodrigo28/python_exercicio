menu = [
    "Menu: ",
    "1. Opção A", 
    "2. Opção B", 
    "3. Sair"
]

opcao_selecionada = 0

while opcao_selecionada != 3:
    print("\n " .join(menu))
    opcao_selecionada = int(input("Informe a opção deseja [1-3]: "))

    if opcao_selecionada == 1:
        nome = input("Informe o seu nome: ")
        print(f"O nome informado foi {nome}")

        input("Enter para continuar ...")
    elif opcao_selecionada == 2:
        email = input("Informe seu email:")
        print(f"O e-mail informado foi {email}")
        input("Enter para continuar ...")
    elif opcao_selecionada == 3:
        print("Saindo ...")
        input("Enter para continuar ...")
print("Fim")