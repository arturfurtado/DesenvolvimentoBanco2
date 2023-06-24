from pymongo import MongoClient

class CarSystem:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client["car_system"]
        self.marcas_collection = self.db["marcas"]
        self.modelos_collection = self.db["modelos"]
        self.carros_collection = self.db["carros"]

    # CRUD em marca
    def create_marca(self, marca):
        result = self.marcas_collection.insert_one(marca)
        return result.inserted_id

    def read_marca(self, marca_id):
        marca = self.marcas_collection.find_one({"_id": marca_id})
        return marca

    def update_marca(self, marca_id, new_marca):
        result = self.marcas_collection.update_one({"_id": marca_id}, {"$set": new_marca})
        return result.modified_count > 0

    def delete_marca(self, marca_id):
        result = self.marcas_collection.delete_one({"_id": marca_id})
        return result.deleted_count > 0

    def get_all_marcas(self):
        marcas = self.marcas_collection.find()
        return list(marcas)

    # CRUD em modelo
    def create_modelo(self, modelo):
        result = self.modelos_collection.insert_one(modelo)
        return result.inserted_id

    def read_modelo(self, modelo_id):
        modelo = self.modelos_collection.find_one({"_id": modelo_id})
        return modelo

    def update_modelo(self, modelo_id, new_modelo):
        result = self.modelos_collection.update_one({"_id": modelo_id}, {"$set": new_modelo})
        return result.modified_count > 0

    def delete_modelo(self, modelo_id):
        result = self.modelos_collection.delete_one({"_id": modelo_id})
        return result.deleted_count > 0

    def get_all_modelos(self):
        modelos = self.modelos_collection.find()
        return list(modelos)

    # CRUD em carro
    def create_carro(self, carro):
        result = self.carros_collection.insert_one(carro)
        return result.inserted_id

    def read_carro(self, carro_id):
        carro = self.carros_collection.find_one({"_id": carro_id})
        return carro

    def update_carro(self, carro_id, new_carro):
        result = self.carros_collection.update_one({"_id": carro_id}, {"$set": new_carro})
        return result.modified_count > 0

    def delete_carro(self, carro_id):
        result = self.carros_collection.delete_one({"_id": carro_id})
        return result.deleted_count > 0

    def get_all_carros(self):
        carros = self.carros_collection.find()
        return list(carros)


# Exemplo de uso
connection_string = "mongodb://localhost:27017"
car_system = CarSystem(connection_string)

marca_data = {
    "nome": "Ford"
}
marca_id = car_system.create_marca(marca_data)
print(f"Created Marca with ID: {marca_id}")

marca = car_system.read_marca(marca_id)
print(f"Read Marca: {marca}")

updated_marca_data = {
    "nome": "Ford Motors"
}
update_result = car_system.update_marca(marca_id, updated_marca_data)
print(f"Update Marca successful: {update_result}")

delete_result = car_system.delete_marca(marca_id)
print(f"Delete Marca successful: {delete_result}")

# Obter todas as marcas
marcas = car_system.get_all_marcas()
print("All Marcas:")
for marca in marcas:
    print(marca)

# Obter todos os modelos
modelos = car_system.get_all_modelos()
print("All Modelos:")
for modelo in modelos: 
    print(modelo)

# Obter todos os carros
carros = car_system.get_all_carros()
print("All Carros:")
for carro in carros:
    print(carro)

# Exemplo de inserção de valores em carro
carro_data = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2022,
    "cor": "vermelho",
    "preco": 250000
}

carro_id = car_system.create_carro(carro_data)
print(f"Created Carro with ID: {carro_id}")

# Exemplo de inserção de valores em modelo
modelo_data = {
    "marca": "Chevrolet",
    "nome": "Corsa",
    "ano_fabricacao": 2022,
    "potencia": 450,
    "tipo": "esportivo"
}

modelo_id = car_system.create_modelo(modelo_data)
print(f"Created Modelo with ID: {modelo_id}")
