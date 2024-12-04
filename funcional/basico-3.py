def remover_nome(nome):
    def remover_na_lista(lista):
        return [n for n in lista if n != nome]
    return remover_na_lista

remover_maria = remover_nome("Maria")
remover_joao  = remover_nome("João")

lista_1 = ["Ana",  "Pedro",    "Maria",   "João",   "Cardoso"]
lista_2 = ["João", "Stefanni", "Izadora", "Carlos", "Vagner"]

print(remover_maria(lista_1))
print(remover_joao(lista_2))
print(remover_nome("Izadora")(lista_2))