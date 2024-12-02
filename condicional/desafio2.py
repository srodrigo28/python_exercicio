# ler 3 valores e pegar imprir os valores menor e maior

registro1 = float(input("digite valor1 "))
registro2 = float(input("digite valor2 "))
registro3 = float(input("digite valor3 "))

if registro1 > registro2 and registro1 > registro3:
    maior = registro1
elif registro2 > registro1 and registro2 > registro3:
    maior = registro2
elif registro3 > registro2 and registro3 > registro1:
    maior = registro3

if registro1 < registro2 and registro1 < registro3:
    menor = registro1
elif registro2 < registro1 and registro2 < registro3:
    menor = registro2
elif registro3 < registro2 and registro3 < registro1:
    menor = registro3
print(f"O maior é {maior}")
print(f"O menor é {menor}")