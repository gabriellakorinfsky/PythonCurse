import socket

resp = "S"

while(resp == "S"):
    url = input("Digite uma url: ")
    # gethostbyname funciona sem o http ou https
    ip = socket.gethostbyname(url)
    print("O IP referente à URL informada é: ", ip)
    resp = input("Digite <S> para continuar: ").upper()