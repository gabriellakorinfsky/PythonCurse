nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

# upper converte o conteudo de uma "string" para letra maiuscula, ou seja, o que foi digitado no "input" ficará
# em caixa alta
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? sim ou não? ").upper()

if idade >= 65:
    print("\nPaciente COM PRIORIDADE!")
    if doenca_infectocontagiosa == "SIM":
        print("Encamenhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encamenhe o paciente para sala BRANCA")
    else:
        print("\nResponda a suspeita de doença infectocontagiosa com SIM ou NÃO!")

else:
    print("\nPaciente SEM PRIORIDADE!")
    if doenca_infectocontagiosa == "SIM":
        print("Encamenhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NÃO":
        print("Encamenhe o paciente para sala BRANCA")
    else:
        print("\nResponda a suspeita de doença infectocontagiosa com SIM ou NÃO!")

# Entre decisao composta do (DecisaoCompostaBool.py) e DecisaoEncadeada é melhor usar a encadeada pois se tivessemos
# mais condições do que apenas (idade e doenca) seria usado muitos if's e elifs com uma grande chance de erro
# em uma das linhas, portanto é melhor usar a encadeada por boas práticas, pois facilita a leitura e isola as ações
