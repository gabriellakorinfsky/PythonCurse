# modulo solicitará o nivel de acesso da pessoa que pode ser (ADM, USR ou GUEST)
# ADM exibir "Olá administrador" ou "Olá administradora"
# USR exibir "Olá usuário" ou "Olá usuária"
# GUEST exibir "Olá usuário" ou "Olá visitante"
# se diferente dos de cima deve exibir "Olá desconhecido"
# Considerar apenas feminino e masculino

nivelDeAcesso = input("Digite seu nível de acesso (ADM, USR, GUEST ou outro): ").upper()
genero = input("Digite seu gênero ( F / M ): ").upper()

if genero == "M":
    if nivelDeAcesso == "ADM":
        print("Olá administrador!")
    elif nivelDeAcesso == "USR":
        print("Olá Usuário")
    elif nivelDeAcesso == "GUEST":
        print("Olá Visitante!")
    else:
        print("Olá Desconhecido")
else:
    if genero == "F":
        if nivelDeAcesso == "ADM":
            print("Olá administradora!")
        elif nivelDeAcesso == "USR":
            print("Olá Usuária")
        elif nivelDeAcesso == "GUEST":
            print("Olá Visitante!")
        else:
            print("Olá Desconhecida")
    else:
        print("Responda com ADM, USR, GUEST ou outro")





