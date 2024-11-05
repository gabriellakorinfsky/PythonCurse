# Preencher o Inventario
def preencherInventario(lista):
    resp = "s"
    while resp == "s":
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite 's' para continuar: ").upper()

# Exibir Inventário
def exibirInventario(lista):
    for elemento in lista:
        print("\nEquipamentos: ", elemento[0])
        print("Valor.......: ", elemento[1])
        print("Serial......: ", elemento[2])
        print("Departamento: ", elemento[3])
    
# Localiza nome
def localizarPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja: ")

    for elemento in lista:
        if busca  == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.: ", elemento[2])
            
# Depreciar por nome
def depreciarPorNome(lista, porc):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")

    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Valor atual: ", elemento[1])    
                
# Excluir por numero serial
def excluirPorSerial(lista):
    deletar = int(input("Digite o numero serial do equipamento que deseja deletar: "))

    for elemento in lista:
        if elemento[2] == deletar:
            lista.remove(elemento)
            
    return "Itens excluídos"

# Resumir valores
def resumirValores(lista):
    valores = []
    
    for elemento in lista:
        valores.append(elemento[1])
    
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa", min(valores))
        print("O total de equipamentos é de: ", sum(valores))