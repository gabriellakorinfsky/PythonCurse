#nome = "Gabriella Lacerda"
#empresa = 'FIAP'
#qtde_funcionarios = 500
#mediaMensalidade = 856.50

nome = input("Digite o nome do funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print("\n" + nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("\n ================== Verifique os tipos de dados: ================== ")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))