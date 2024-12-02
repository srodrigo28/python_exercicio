print(" 1. Iniciando com lista")
lista = ["go", "df", "sp", "mg", "rj"]

for numero in lista:
    print(numero, end=" ")

for i, numero in enumerate(lista):
    print(f"\n({i}, {numero})", end=" ")
