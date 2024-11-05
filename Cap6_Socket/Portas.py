import socket

# Retorno das portas que estamos disponibilizando para:
# Dominio (padrão 53), usado para resolver a conversão entre DNS e IP
print(socket.getservbyname("domain"))
# HTTP (padrão 80), usado para navegar nas páginas WEB
print(socket.getservbyname("http"))
# FTP (padrão 21), usado para transferência de arquivos
print(socket.getservbyname("ftp"))