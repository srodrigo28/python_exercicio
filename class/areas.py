class Areas:
    PI = 3.14
    valor = 0

    @staticmethod
    def circulo(raio=1):
        return Areas.PI * (raio ** 2)
    
    def quadrado(lado=1, altura=1):
        return lado * altura

    def triangle(base=1, altura=1):
        return( base * altura ) / 2
    
    @classmethod
    def alterar_valor(cls, novo_valor):
        cls.valor = novo_valor

Areas.alterar_valor(10)
# print(Areas.PI)
print(Areas.quadrado(2, 3))
print(Areas.valor)
# print(Areas.circulo(2.5))