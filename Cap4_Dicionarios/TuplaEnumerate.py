# Dicionario
usuarios = {}
resp = "S"
# É uma lista
emails = []

while resp == "S":
    emails.append(input("Digite um email: ").lower())
    resp = input("Digite 'S' para continuar: ").upper()
    
tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print("\nEmail: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome: "), input("Digite o nível: ")]
    
for chave,dado in usuarios.items():
    print("\nUsuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])