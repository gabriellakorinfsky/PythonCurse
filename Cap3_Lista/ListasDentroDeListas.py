
inventario = []
resposta = "S"

while resposta == "S":
    # Cria a lista equipamentos
    equipamento = [
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")
    ]
    # A lista equipamento vai ser armazenada no inventario
    inventario.append(equipamento)
    resposta = input("Digite 'S' para continuar: ").upper()
 
# Vai apresentar todos os elementos do inventario que são os equipamentos   
# Inventario [
#   1 Equipamento[Equipamento, Valor, serial, depart]   
#   2 Equipamento[Equipamento, Valor, serial, depart]
#]
# Elemento se refere as posições da lista de equipamento
for elemento in inventario:
    print("\nEquipamentos: ", elemento[0])
    print("Valor.......: ", elemento[1])
    print("Serial......: ", elemento[2])
    print("Departamento: ", elemento[3])

# Buscar o produto
busca = input("Digite o nome do equipamento que deseja: ")

for elemento in inventario:
    if busca  == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.: ", elemento[2])

# Alterar os valores do produto    
depreciacao = input("Digite o nome do equipamento que será depreciado: ")

for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Valor atual: ", elemento[1])        

# Deletar a lista do produto específico        
deletar = int(input("Digite o numero serial do equipamento que deseja deletar: "))

for elemento in inventario:
    if elemento[2] == deletar:
        inventario.remove(elemento)

for elemento in inventario:
    print("\nEquipamentos: ", elemento[0])
    print("Valor.......: ", elemento[1])
    print("Serial......: ", elemento[2])
    print("Departamento: ", elemento[3])
    
valores = []
# Armazena apenas os valores dos elementos
for elemento in inventario:
    valores.append(elemento[1])
# Diz o min, max e a soma dos valores dos produtos
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa", min(valores))
    print("O total de equipamentos é de: ", sum(valores))