# Criar Listas
# As listas podem iniciar vazias ou com dados

# Lista preenchida estaticamente

lista_estatica = ["xpto", True]
print(lista_estatica)

# Lista preenchida dinamicamente
# Input retorna uma string, deve converter o dado para int, para, entao, posteriormente
# converter para bool. 

lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado?")))]
print(lista_dinamica)

# Lista vazia

lista_vazia = []
print(lista_vazia)