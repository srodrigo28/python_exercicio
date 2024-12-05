class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

p1 = Pessoa("amanda", 22, 162)
p2 = Pessoa("joão", 25, 1.75)

print(f"Nome: {p1.nome}, idade: {p1.idade}, altura: {p1.altura}")