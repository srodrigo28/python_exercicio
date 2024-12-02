print(" 1. Iniciando com lista")
lista = [1, 2, 3, 4, 5]

for numero in lista:
    print(numero, end=" ")

for i, numero in enumerate(lista):
    print(f"({i}, {numero})", end=" ")


print("\n 2. Iniciando com tupla")
tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    print(numero, end=" ")

print("\n 3. Iniciando com conjunto")
conjunto = {1, 2, 3, 4, 5}
for numero in conjunto:
    print(numero, end=" ")