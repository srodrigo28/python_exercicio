# Solicite ao usuário o total de uma conta de restaurante.
# E a porcentagem de gorjeta que ele gostaria de pagar.
# Calcule e mostre o valor total da conta.
# Mostre o valor da Gorjeta.
# Mostre o valor total a pagar.

valor = float(input('Valor total (R$): '))
gorjeta = float(input('Percentual da Gorjeta (0-100): '))
valor_gorjeta = valor * gorjeta / 100
valor_final = valor + valor_gorjeta
print(f'O valor final da conta é R$ {valor_final}')