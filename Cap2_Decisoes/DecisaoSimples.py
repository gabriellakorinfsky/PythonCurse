nome = input("Digite o nome: ")
idade = int (input("Digite a idade: "))
prioridade = "NÃO"

#deve ser encerrado com dois pontos ( : )
#as linhas com recuo após o "if" <TAB> só funcionaram se a condição for verdadeira
#se tirar o recuo, volta ao codigo normal
if idade >= 65:
    prioridade = "SIM"

print("\nO paciente " + nome + " possui atendimento prioritário? " + prioridade)
