equipamentos = []
valores = []
seriais = []
departamentos = []

resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()
    print("")
   
busca = input("\nDigite o nome do equipamento que deseja buscar: ")    

depreciacao = input("\nDigite o nome do equipamento que sofrerá 10% de depreciação: ")

danificado = int(input("\Digite o serial do equipamento que será excluido: "))

# Indice vai de 0 até a quantidade total de equipamentos
for indice in range(0,len(equipamentos)):
    
    # Se busca for igual a algum equipamento nos indices
    if busca == equipamentos[indice]:
        print("Número......: ", (indice+1))
        print("\nEquipamentos: ", equipamentos[indice])
        print("Valor.......: ", valores[indice])
        print("Serial......: ", seriais[indice])
        print("Departamento: ", departamentos[indice])

    # Alterar valora do equipamento
    if depreciacao == equipamentos[indice]:
        print("\nValor antigo: ", valores[indice])
        valores[indice]= valores[indice]*0.9
        print("Valor atual: ", valores[indice])
        
    # Deletar da lista
    if seriais[indice] == danificado:
        print("Deletar equipamento")
        del departamentos[indice]
        del valores[indice]
        del seriais[indice]
        del departamentos[indice]
        break
        
    
