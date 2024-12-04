def repetir(funcao, qtde=2):
    for _ in range(qtde):
        funcao()

def bom_dia():
    print("Boa noite!")

repetir(bom_dia, 6)