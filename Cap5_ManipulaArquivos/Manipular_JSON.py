import sys
sys.path.append("D:\\WORK\\Python\\FIAP-Python")
from Funcoes import Funcoes_JSON 
F = Funcoes_JSON

inventario = F.ler_arquivo("inventaro_json.json")
opcao = F.chamarMenu()
while opcao>0 and opcao<3:
    if opcao == 1:
        print(F.registrar(inventario, "inventario_json.json"))
    elif opcao == 2:
        F.exibir("inventario_json.json")
    opcao = F.chamarMenu()