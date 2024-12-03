from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import random

def criar_senha(tamanho, maiusculas, minusculas, numeros, simbolos):
    caracteres = "".join([
        ascii_uppercase if maiusculas else "",
        ascii_lowercase if minusculas else "",
        digits if numeros else "",
        punctuation if simbolos else "",
    ])

    senha = random.choices(caracteres, k=tamanho)
    senha = "".join(senha)
    return senha

nova_senha = criar_senha(
    tamanho=3,
    maiusculas=False,
    minusculas=True,
    numeros=True,
    simbolos=False
)
print(nova_senha)