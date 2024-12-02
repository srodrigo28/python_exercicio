# exemplo 1
# base_dois = []
# indice = 2
# for x in range(1, 14):
#     base_dois.append(indice ** x)

# print(base_dois)

# exemplo 2
# base_dois = [ 2 ** x for x in range(1, 14)]
# print(base_dois)

# exemplo 3
# base_dois = [2 ** x for x in range(1, 21) if x % 2 == 0]
# print(base_dois)

# exemplo 4
numeros = [ x * x for x in range(1, 30) if x % 3 != 0]
print(numeros)