class Funcionario:
    def __init__(self, nome, salario, idade=18):
        self.__nome = nome
        self.__salario = salario
        self.__idade = idade
    
    def get_nome(self):
        return self.__nome
    def get_salario(self):
        return self.__salario
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade_nova):
        if idade_nova > 18:
            raise ValueError("A idade deve ser maior que 18 e menor que 70")
        self.__idade = idade_nova

func = Funcionario('maria', 1000, 16 )
print(func.get_nome())
print(func.get_salario())
print(func.idade)
