from pymongo import MongoClient
from bson.objectid import ObjectId
from Model.animal import Animal

class ZoologicoDAO:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_animal(self,animal: Animal) -> str:
        try:
            result = self.collection.insert_one({"id": animal.id,"nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": animal.habitat})
            animal_id = str(result.inserted_id)
            print(f"Animal {animal.nome} created with id: {animal.id}")
            return animal_id
        except Exception as error:
            print(f"An error occurred while creating an animal: {error}")

    def read_animal_by_id(self, animal_id: str) -> dict:
        try:
            animal = self.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No Animal found with id {animal_id}")
        except Exception as error:
            print(f"An error occurred while reading an animal: {error}")

    def update_animal(self, animal_id: str, animal: Animal) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(animal_id)}, {"$set": {"id": animal.id, "nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": animal.habitat}})
            if result.modified_count:
                print(f"Animal {animal_id} updated with name {animal.nome} and especie {animal.especie}, age {animal.idade} and habitat {animal.habitat}")
            else:
                print(f"No animal found with id {animal_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating an animal: {error}")
    def delete_animal(self, animal_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting an animal: {error}")