funcitonario = {
    "nome": "Gustavo",
    "salario": 7655.22,
    "idade": 35,
    "ativo": True
}

for item in funcitonario.keys():
    print(item, ":", funcitonario[item])

for valor in funcitonario.values():
    print(valor)

for chave, valor in funcitonario.items():
    print(chave, "=>", valor)
