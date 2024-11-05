import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMAD" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login negado")

# a senha escondida só funciona no interative window