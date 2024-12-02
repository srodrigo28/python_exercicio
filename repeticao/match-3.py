nome = "Sebastião Rodrigo Nascimento Bastos"
partes_nome = nome.split()

print(partes_nome)

match partes_nome:
    case [primeiro]:
        sigla = primeiro[0:2]
    case [primeiro, *m, ultimo]:
        sigla = primeiro[0] + ultimo[0]
    case _:
        sigla = "AL"
print(f"A sigla do usuário é {sigla.upper()}")