# É criada uma variavel "numero" dentro do "for" e dizemos que de acordo com a função "range()" (que permite
# especificar uma faixa de valores e como será incrementada, a var inciará com o valo 1 até o valor que for digitado
# e a faixa será incrementada de 1 em 1. O conteúdo será repetido até que atinja o valor máximo que for digitado
# Esse laço não é adequado para preenchimento de dados de um projeto, como cadastro, isso é melhor para "while"
# pois ele é usado para save quantos usuarios serão cadastrados, mas o "for" é usado quando esses dados já existem
# e precisamos simplesmente exibi-los ou realizar uma pesquisa dentro deles

for numero in range(1, int(input("Digite um numero para determinar o fim: ")), 1):
    print("\t" + str(numero))
