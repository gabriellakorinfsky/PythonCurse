numero = int(input("Digite um numero: "))
while numero < 100:
    # O numero que for colocado irá aparecer o "numero" até 99
    # "\t" é para acrescentar uma tab antes
    # "\n" é para pular linha
    print("\t" + str(numero))
    # n=n+1 é o que faz o "while" seja finito, pois a condição continua desde que o valor da variavel "n" seja
    # menor que 100. Quando chegar ao valor 99 ele encerrará
    # caso ele não exista, será um loop infinito
    # n+=1 é a mesma coisa
    # O "1" pode ser alterado por outro, aí ele iniciará pelo número que vc colocou
    numero = numero + 1
    # Caso o valor digitado seja maior ou igual a 100, nada acontecerá o pulará para "Laço encerrado"
print("Laço encerrado....")