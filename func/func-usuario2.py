import secrets
from datetime import datetime

def criar_usuario(**atributtos):
    novo_usuario = {
        "nome": "",
        "email": "",
        "senha": secrets.token_urlsafe(6),
        "data_criacao ": datetime.now(),
        "ativo": True
    }

    novo_usuario.update(atributtos)
    return novo_usuario

novo_usuario = criar_usuario(
    nome="Amanda Soares",
    email="amandasoares@gmail.com"   
)

print(novo_usuario)