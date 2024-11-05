# Esse também serve:
# opcao = input("\nO que você deseja?\n ( I ) - Inserir\n ( P ) - Pesquisar\n ( E ) - Excluir\n ( L ) - Listar\n (   ) - Sair\nDigite: ").upper()
# Funciona se for do mesmo diretorio "import Funcoes_Dicionarios"

import sys
sys.path.append("D:\\WORK\\Python\\FIAP-Python")
from Funcoes import Funcoes_Arquivos

F = Funcoes_Arquivos
usuarios={}
opcao = F.perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        F.inserir(usuarios)
    
    if opcao == "P":
        F.pesquisar(input("\nQual matricula deseja pesquisar? ").upper(), usuarios)
    
    if opcao == "E":
        F.excluir(input("\nQual matricula deseja excluir? ").upper(), usuarios)
    
    if opcao == "L":
        F.listar(usuarios)
    
    opcao = F.perguntar()
    
# Metodos para dicionarios: items(), values(), keys(), has_keys(), clear(), popitem()

# items(): retorna em forma de lista - [chave] = [valor]
# values():  retorna em forma de lista apenas os valores sem a chave - ["nome", "data", "estacao"]
# has_keys(): ele permite saber se a chave existe ou não dentro do dicionario, ele retorna true ou false
# clear(): ele limpa o dicionario
# popitem(): montar dicionario que contenha elementos executaveis
        
