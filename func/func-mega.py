import random

def gerar_aposta_mega(qtde):
    aposta = []

    if 6 <= qtde <= 20:
        aposta = random.sample(range(1, 61), qtde)
        aposta.sort()

    return aposta

print(gerar_aposta_mega(6))
print(gerar_aposta_mega(8))
print(gerar_aposta_mega(15))