# Dicionario vazio
usuarios = {}
# Dicionario preenchido
usuarios = {
    "Chaves":["Chaves Silva", "17/06/2017", "Recep_01"],
    "Quico":["Enrico Flores", "03/06/2017", "Raiox_02"],
    "Quico":["Enrico Flores", "03/06/1976", "Raiox_03"]
}

# Também pode ser adicionado dessa forma
# Normalmente usado quando quer adicionar objetos por objetos
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"] = ["Florinda Flores", "26/11/2016", "Recep_01"]
# Se houver chaves iguais o ultimo colocado é o que será armazenado

# Apresenta todos os dados armazenados
print(usuarios)
print("############============############")
# Mostra apenas os dados da chave "Chaves"
print("Dados: ", usuarios.get("Chaves"))