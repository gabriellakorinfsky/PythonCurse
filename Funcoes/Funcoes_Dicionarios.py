
def perguntar():
    resposta = input("\nO que você deseja?\n"
                    +
                    "( I ) - Inserir\n"
                    +
                    "( P ) - Pesquisar\n"
                    +
                    "( E ) - Excluir\n"
                    +
                    "( L ) - Listar\n"
                    +
                    "(   ) - Sair\n"
                    +
                    "Digite: ").upper()
    return resposta
    
def inserir(dicionario):
    chave = input("\nDigite sua matricula: ").upper()
    dicionario[chave] = [
                        input("Digite seu login: ").upper(),
                        input("Digite seu nome: ").upper(),
                        input("Nível do usuario: ").upper(),
                        input("Digite a hora do login: ").upper(),
                        input("Digite a última data de acesso: "),
                        input("Qual a última estação acessada: ").upper()]
    
def pesquisar(chave, dicionario):
    lista = dicionario.get(chave)
    if lista != None:
        print("\nLogin...........:" + lista[0])
        print("Nome............: " + lista[1])
        print("Nível do usuário: " + lista[2])
        print("Hora do login...: " + lista[3])
        print("Último acesso...: " + lista[4])
        print("Última estação..: " + lista[5])
        
        
def excluir(chave, dicionario):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("\nObjeto Eliminado")
    
def listar(dicionario):
    for chave, valor in dicionario.items():
        print("\nObjeto.......................")
        print("Matricula: ", chave)
        print("Dados....: ", valor)