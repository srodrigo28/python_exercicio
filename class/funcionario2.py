class FuncionarioV2:
    def __init__(self, salario):
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    def movimentacao_salarial(self, percentual):
        if percentual < 0:
            raise ValueError("Percentual inválido")
        self.__salario = self.__salario + (self.__salario * percentual / 100)

f1 = FuncionarioV2(1500)
f1.movimentacao_salarial(-50)
print(f1.salario)
