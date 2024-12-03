from datetime import datetime

def hora_atual():
    agora = datetime.now()
    return agora.hour

user = input("Seu nome: ")
def saudacao():
    hora = hora_atual()

    match hora:
        case h if h in range(0, 6):
            s = f"Boa madrugada {user}"
        case h if h in range(6, 12):
            s = f"Bom dia {user}"
        case h if h in range(12, 18):
            s = f"Boa tarde {user}"
        case _:
            s = f"Boa noite {user}"
    return s

rs = saudacao()
print(rs)