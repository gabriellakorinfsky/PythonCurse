# Lista armazena um numero indeterminado de dados

inventario = []
resposta="S"

# append adiciona mais itens a lista
while resposta=="S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()
    print("")

# Elemento vai percorrer a lista
for elemento in inventario:
    print(elemento)