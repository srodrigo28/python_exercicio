class Carro:
    def __init__(self, marca, nome):
        self.marca = marca
        self.nome = nome

c1 = Carro("Fiat", "Bravo")
c2 = Carro("Forde", "Fusion")

print(f" {c1.nome} - {c1.marca}")
print(f" {c2.nome} - {c2.marca}")