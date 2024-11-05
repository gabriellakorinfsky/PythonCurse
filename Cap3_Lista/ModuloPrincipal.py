# Esse comando funciona no pycharm
# from Cap3_Listas.IndentificacaoDeFuncao import *
import IdentificacaoDeFuncao

minhaLista=[]
print("Preenchendo")
IdentificacaoDeFuncao.preencherInventario(minhaLista)
print("Exibindo")
IdentificacaoDeFuncao.exibirInventario(minhaLista)

print("Pesquisando")
IdentificacaoDeFuncao.localizarPorNome(minhaLista)
print("Alterando")
IdentificacaoDeFuncao.depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(IdentificacaoDeFuncao.excluirPorSerial(minhaLista))
IdentificacaoDeFuncao.exibirInventario(minhaLista)

print("Resumindo")
IdentificacaoDeFuncao.resumirValores(minhaLista)