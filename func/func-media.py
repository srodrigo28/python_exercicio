# exemplo 1
# def calcular_media(a, b, c):
#    return(a + b + c) / 3

# exemplo 2
def calcular_media(*n):
    return sum(n) / len(n)

media = calcular_media(7,9.2,5.8, 10, 11, 9.5, 7.2)
print(f"O valor da média é {media:.2f}")