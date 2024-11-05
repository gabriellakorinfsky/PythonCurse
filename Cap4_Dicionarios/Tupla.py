# Estrutura para dados voláteis, assim como as variáveis, listas e dicionário.
# Tupla = Não aceita alteração
# sempre representadas com seus dados entre parênteses
# Normalmente usado para realizar leitura de uma resposta de pyhton e não de dados inseridos
# Não são os mais usados por programadores

#Dicionario
ips = {}
resp = "S"

while resp == "S":
    ips[(input("Digite os dois primeiros octeto: "),
         input("Digite os dois últimos octetos: "))] = input("\nNome da máquina: ")
    resp = input("Digite 'S' para continuar: ").upper()
    
print("\nExibindo ip's: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])
    
print("\nExibindo maquinas com o mesmo endereço: ")
pesquisa=input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    print("\nMáquinas no mesmo endereço(redes diferentes)")
    if(ip[1]==pesquisa):
        print(nome)
        
print("Exibindo as máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)