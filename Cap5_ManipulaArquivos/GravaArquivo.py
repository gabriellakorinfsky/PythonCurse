# o with junto ao open(), o controle de encerramento do arquivo em memoria ficara por conta do comando with

with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")
    
with open("teste.txt", "a") as arquivo:
    arquivo.write("continuação do texto.")