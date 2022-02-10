# importando a biblioteca regex
import re

# Expressão regular com as regras de validação do email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Criando a função
def check(email):
    # Somente se toda a expressão for verdadeira o email será valido
    if (re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Inserindo o email para verificação
if __name__ == '__main__':
    # Entrada do email
    email = input("Insira seu email: ")
    # Chamando a função
    check(email)
