import getpass
from datetime import datetime

print("\nUsuário.......: ", getpass.getuser())
print("Data Completa.: ", datetime.now())
print("Dia...........: ", datetime.now().day)
print("Mês...........: ", datetime.now().month)
print("Ano...........: ", datetime.now().year)
print("Hora..........: ", datetime.now().hour)
print("Minute........: ", datetime.now().minute)
print("Segundo.......: ", datetime.now().second)
print("\n")