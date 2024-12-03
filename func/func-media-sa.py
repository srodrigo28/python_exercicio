def obter_cargos():
    return[
        {"cargos": "Pacoteiro", "qtde": 5, "salario": 1100},
        {"cargos": "atendente", "qtde": 16, "salario": 2000},
        {"cargos": "Gerente", "qtde":   3, "salario": 5000},
        {"cargos": "Diretor", "qtde":   1, "salario": 12500},
    ]

def media_salarial(cargos):
    total_salarial = 0
    qtde_funcionarios = 0

    for cargo in cargos:
        total_salarial += cargo["qtde"] * cargo["salario"]
        qtde_funcionarios += cargo["qtde"]
    return total_salarial / qtde_funcionarios

cargos = obter_cargos()
media = media_salarial(cargos)
print(f"A média salarial é R$ {media:.2f}")