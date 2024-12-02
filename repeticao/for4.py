numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n" "primeira maneira de imprir")
for n in numeros:
    print(n, end=" ")

print("\n")
# usando o continue imprimindo impar
for x in numeros:
    if x % 2 == 0:
        continue
    print(x, end=" ", )
print("\n" "segunda maneira de imprir")

# usando imprimindo impar
for x in numeros:
    if x % 2 != 0:
        print(x, end=" ")