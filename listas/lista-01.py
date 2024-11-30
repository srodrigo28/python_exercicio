numeros = [1, 2, 3, 4]
#print(numeros)

frutas = ['maça', 'banana', 'uva', 'pera']
# print(frutas)
# print(frutas[0])
# frutas.append('abacate')
frutas.insert(0, 'amexa')
frutas.remove('maça')
# print(frutas)

listaMista = ['janeiro', 2024, True, ['notebook', 10, 2500]]
#print(listaMista)
#print(listaMista[3][2])

pilha_count = [1, 2, 3]
# print(f'tirando ... {pilha_count.pop()}')
# print(len(pilha_count))

pilha_frutas = ['uva', 'banana', 'laranja']
# print(f'tirando ... {pilha_frutas.pop()}')
# print(len(pilha_frutas))

# retirando ultimo da fila até acabar
pilha_frutas2 = ["uva", "banana", "laranja"]
print(f'lista total {len(pilha_frutas2)}')
print(f"tirando ... {pilha_frutas2.pop()}")
print(f"tirando ... {pilha_frutas2.pop()}")
print(f"tirando ... {pilha_frutas2.pop()}")
print(f'lista total {len(pilha_frutas2)}')
print(pilha_frutas2)

# tira primeira posição da fila
lista_entrega = ['amanda', 'eduardo', 'fernando', 'maria', 'angelica']
# print(len(lista_entrega))
# print(f'Qual e o da vez {lista_entrega.pop(0)} ?')
# print(f'Qual e o da vez {lista_entrega.pop(0)} ?')
# print(f'Qual e o da vez {lista_entrega.pop(0)} ?')
# print(len(lista_entrega))