nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

#upper converte o conteudo de uma string para letra maiuscula, ou seja, o que foi digitado no input ficará em caixa alta
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? sim ou não? ").upper()

if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("\nO paciente " + nome + " será direcionado para sala AMARELA - COM PRIORIDADE!")
# elif = else + if é como uma segunda condição
# = é atribuição == é comparação
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("\nO paciente " + nome + " será direcionado para sala AMARELA - SEM PRIORIDADE!")
elif idade >= 65 and doenca_infectocontagiosa == "NÃO":
    print("\nO paciente " + nome + " será direcionado para sala BRANCA - COM PRIORIDADE!")
elif idade < 65 and doenca_infectocontagiosa == "NÃO":
    print("\nO paciente " + nome + " será direcionado para sala BRANCA - SEM PRIORIDADE!")
# else só será executado se a primeira e segunda condição for falsa
else:
    print("\nResponda a suspeita de doença infectocontagiosa com SIM ou NÃO!")
