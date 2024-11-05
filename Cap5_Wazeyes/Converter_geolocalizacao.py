import sys
sys.path.append("D:\\WORK\\Python\\FIAP-Python")
from geopy.geocoders import Nominatim
from Funcoes import Funcoes_JSON

F = Funcoes_JSON

geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
dicionario = F.ler_arquivo("entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + "," + lista[1] + " " +lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
saida = {"coordenadas": (location.latitude, location.longitude)}
F.gravar_arquivo(saida, "saida.json")
    