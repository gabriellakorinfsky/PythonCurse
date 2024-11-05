from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco=input("\nDigite um endereco com número e cidade.\n"
            "Exemplo: avenida paulista, 100 São Paulo\n"
            ">>> ")

resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    print("\nEndereço completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Regiao............: ", resultado[3])