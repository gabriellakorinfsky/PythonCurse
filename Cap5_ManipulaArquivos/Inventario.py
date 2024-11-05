import sys
sys.path.append("D:\\WORK\\Python\\FIAP-Python")
from Funcoes import Funcoes_Arquivos

F = Funcoes_Arquivos

inventario = {}

opcao = F.chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        F.registrar(inventario)
    elif opcao == 2:
        F.persistir(inventario)
    elif opcao == 3:
        resultado = F.exibir()
        for linha in resultado:
            # 2 porque vai tirar o nº de patrimonio se for apenas uma casa e ";", vai aparecer todo o resto.
            # no caso ele pula dois caracteres 1; , se for 100; , iria ficar 0;
            #  -1 é representado para dizer que vai mostrar até o final da linha
            # print(linha[2:-1])
            
            # O 2 foi substituido pelo metodo find(), ele irá retornar a primeira posição do ";" encontrado e acrescentará +1
            # para que não exiba ele próprio.
            #print(linha[linha.find(";")+1:-1])
   
            # separacao=linha[linha.find(";")+1:-1]
            # data=separacao[0:separacao.find(";")]
            # separacao = separacao[separacao.find(";")+1:-1]
            # descricao=separacao[0:separacao.find(";")]
            # o rfind() ele ler da direita pra esquerda
            # departamento=linha[linha.rfind(";")+1:-1]
            # print("Data.........: ", data)
            # print("Descrição....: ", descricao)
            # print("Departamento.: ", departamento)
            
            
            # O metodo split() ele cria uma lista separada por ";" e separa o conjunto de caracteres.
            lista = linha.split(";")
            print("Data.........: ", lista[1])
            print("Descrição....: ", lista[2])
            print("Departamento.: ", lista[3])
    opcao = F.chamarMenu()