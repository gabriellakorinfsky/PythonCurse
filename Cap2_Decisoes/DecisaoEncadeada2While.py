continuar = "SIM"
while continuar == "SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? sim ou não? ").upper()

    while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NÃO":
        doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? SIM ou NÃO? ").upper()
        # Primeiro problema: Ver quem são os infectados
        if doenca_infectocontagiosa == "SIM":
            print("Encaminhe o paciente para a sala AMARELA")
        elif doenca_infectocontagiosa == "NÃO":
            print("Encaminhe o paciente para a sala BRANCA")
        else:
            print("Digite SIM ou NÃO!!!")

    # Segundo problema: Informar prioridade para maiores de 64 anos, descobrir o gênero para saber
    # se são mulheres e se são maiores que 10 anos para descobrir se estão gravidas ou não, para saber colocar com
    # prioridade

    if idade >= 65:
        print("Paciente COM PRIORIDADE")
    else:
        genero = input("Digite o gênero do paciente: ").upper()
        if genero == "FEMININO" and idade > 10:
            gravidez = input("A paciente está grávida? ").upper()
            if gravidez == "SIM":
                print("Paciente COM PRIORIDADE")
            else:
                print("Paciente SEM PRIORIDADE")
        else:
            print("Paciente SEM PRIORIDADE")
    continuar = input("Deseja continuar adicinando pacientes? Sim ou Não? ").upper()
