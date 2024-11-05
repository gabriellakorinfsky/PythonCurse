resposta = "SIM"
while resposta == "SIM":
    nivelDeAcesso = input("Digite seu nível de acesso (ADM, USR, GUEST ou outro): ").upper()
    if nivelDeAcesso == "ADM" or nivelDeAcesso == "USR":
        genero = input("Digite seu gênero ( F / M ): ").upper()
        if nivelDeAcesso == "ADM":
            if genero == "F":
                print("Olá Administradora!")
            else:
                print("Olá Administrador!")
        else:
            if genero == "F":
                print("Olá Usuária!")
            else:
                print("Olá Usuário!")
    elif nivelDeAcesso == "GUEST":
        print("Olá Visitante!")
    else:
        print("Olá Desconhecido(a)")
    resposta = input("Digite SIM para continuar: ").upper()




