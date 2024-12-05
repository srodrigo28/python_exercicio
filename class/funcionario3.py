class FuncionarioV3:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    @property
    def nome(self):
        return self.__nome
    @property
    def salario(self):
        return self.__salario
    
    def movimentacao_salarial(self, percentual):
        if percentual < 0:
            raise ValueError("Percentual inválido")
        self.__salario = self.__salario + (self.__salario * percentual / 100)

f1 = FuncionarioV3('maria', 1500)
f1.movimentacao_salarial(37)
print(f"Funcionário: {f1.nome}, {f1.salario}")
