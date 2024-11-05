# w - write
# r - read
# a - append(anexar)
# "a" pode ler e escrever como se fosse um diario
# x - exclusive
# uma vez que criou/abriu o "x" ninguém mais poderá abri-lo
# t - text
# pode ser combinado também b(byte) wb ou w+b


with open("teste.txt", "rb") as arquivo:
    conteudo = arquivo.readlines()

print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo: ", conteudo)