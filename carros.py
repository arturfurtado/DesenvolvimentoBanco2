from pymongo import MongoClient

# Conexão MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["car_system"]
marcas_collection = db["marcas"]
modelos_collection = db["modelos"]
carros_collection = db["carros"]

# CRUD em marca
def create_marca(marca):
    result = marcas_collection.insert_one(marca)
    return result.inserted_id

def read_marca(marca_id):
    marca = marcas_collection.find_one({"_id": marca_id})
    return marca

def update_marca(marca_id, new_marca):
    result = marcas_collection.update_one({"_id": marca_id}, {"$set": new_marca})
    return result.modified_count > 0

def delete_marca(marca_id):
    result = marcas_collection.delete_one({"_id": marca_id})
    return result.deleted_count > 0

def get_all_marcas():
    marcas = marcas_collection.find()
    return list(marcas)

# CRUD em modelo
def create_modelo(modelo):
    result = modelos_collection.insert_one(modelo)
    return result.inserted_id

def read_modelo(modelo_id):
    modelo = modelos_collection.find_one({"_id": modelo_id})
    return modelo

def update_modelo(modelo_id, new_modelo):
    result = modelos_collection.update_one({"_id": modelo_id}, {"$set": new_modelo})
    return result.modified_count > 0

def delete_modelo(modelo_id):
    result = modelos_collection.delete_one({"_id": modelo_id})
    return result.deleted_count > 0

def get_all_modelos():
    modelos = modelos_collection.find()
    return list(modelos)

# CRUD em carro
def create_carro(carro):
    result = carros_collection.insert_one(carro)
    return result.inserted_id

def read_carro(carro_id):
    carro = carros_collection.find_one({"_id": carro_id})
    return carro

def update_carro(carro_id, new_carro):
    result = carros_collection.update_one({"_id": carro_id}, {"$set": new_carro})
    return result.modified_count > 0

def delete_carro(carro_id):
    result = carros_collection.delete_one({"_id": carro_id})
    return result.deleted_count > 0

def get_all_carros():
    carros = carros_collection.find()
    return list(carros)

# Exemplo de uso
marca_data = {
    "nome": "Ford"
}
marca_id = create_marca(marca_data)
print(f"Created Marca with ID: {marca_id}")

marca = read_marca(marca_id)
print(f"Read Marca: {marca}")

updated_marca_data = {
    "nome": "Ford Motors"
}
update_result = update_marca(marca_id, updated_marca_data)
print(f"Update Marca successful: {update_result}")

delete_result = delete_marca(marca_id)
print(f"Delete Marca successful: {delete_result}")

# Obter todas as marcas
marcas = get_all_marcas()
print("All Marcas:")
for marca in marcas:
    print(marca)

# Obter todos os modelos
modelos = get_all_modelos()
print("All Modelos:")
for modelo in modelos:
    print(modelo)

# Obter todos os carros
carros = get_all_carros()
print("All Carros:")
for carro in carros:
    print(carro)
