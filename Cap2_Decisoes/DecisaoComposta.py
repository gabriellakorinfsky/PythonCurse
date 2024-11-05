nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

# por usar menos variaveis comparado ao anterior, utilizamos menos espaço da memória
# o "else" deve estar alinhado com o "if" e ter os dois pontos ( : )
if idade >= 65:
    print("\nO paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("\nO paciente " + nome + " NÃO POSSUI atendimento prioritário!")

# não fazer!!! Pois consumirá um processamento desnecessário
if idade >= 65:
    print("\nO paciente " + nome + " POSSUI atendimento prioritário!")
if idade < 65:
    print("\nO paciente " + nome + " NÃO POSSUI atendimento prioritário!")
