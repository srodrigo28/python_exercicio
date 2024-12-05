class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 10
    def frear(self):
        self.velocidade -= 10
    
    def buzinar(self, qtde=1):
        for i in range(qtde):
            print(f"{self.marca} {self.modelo} => Biiii")

c1 = Carro("Fiat", "Bravo")
c1.buzinar()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c2 = Carro("Forde", "Fusion")

print(f" {c1.modelo} - {c1.marca} - {c1.velocidade} - {c1.buzinar}")
# print(f" {c2.modelo} - {c2.marca} - {c2.velocidade}")