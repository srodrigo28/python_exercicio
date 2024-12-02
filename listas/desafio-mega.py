# Escreva um código em Python que gere os números da mega-sena.
# Primeiramente solicite para o usuário informar a quantidade
# de números da aposta ( entre 6 a 20) e depois gere
# uma lista com o tamanho solicitado com números não repetidos
# entre 1 e 60.

import random
# print(random.random(1, 60))

quantidade = int(input("Informe a quantidade [6-20]: "))

# exemplo 1
# if quantidade >= 6 and quantidade <= 20:
#     print("Aposta válida")
# else:
#     print("Aposta não valida coloque a quantidade de números ")

# exemplo 2
if 6 <= quantidade <= 20:
    print("Aposta válida")
    aposta = []
    while len(aposta) != quantidade: 
        novo_numero = random.randint(1, 60)

        if novo_numero not in aposta:
            aposta.append(novo_numero)
        
    aposta.sort()
    print(f"A posta gerada: {aposta}")
else:
    print("Aposta não valida coloque a quantidade de números ")