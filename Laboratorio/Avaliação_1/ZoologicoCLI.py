from ZoologicoDAO import ZoologicoDAO
from Model.animal import Animal
from Model.cuidador import Cuidador
from Model.habitat import Habitat
from database import Database


class Zoologico:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")
class ZoologicoCLI(Zoologico):
    def __init__(self):
        super().__init__()
        self.add_command("create", self.createAnimal())
        self.add_command("read", self.readAnimal())
        self.add_command("update", self.updateAnimal())
        self.add_command("delete", self.eleteAnimal())
     #entrando com os dados
    def createAnimal(self):

        #entrando com os dados do cuidador
        idCuidador = input("Entre com o Id do cuidador: ")
        nomeCuidador = input("Entre com o nome do cuidador: ")
        documentoCuidador = input("Entre com o documento do cuidador: ")
        cuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)

        #entrando com os dados do habitat
        idHabitat = input("Entre com o Id do habitat: ")
        nomeHabitat = input("Entre com o nome do habitat: ")
        tipoAmbienteHabitat = input("Entre com o tipo de habitat: ")
        habitat = Habitat(idHabitat, nomeHabitat, tipoAmbienteHabitat, cuidador)

        #entrando com os dados do animal
        idAnimal = input("Entre com o Id do animal: ")
        nomeAnimal = input("Entre com o nome do animal: ")
        especieAnimal = input("Entre com a especie do animal: ")
        idadeAnimal = input("Entre com a idade do animal: ")
        animal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, habitat)

        idAnimalCriado = ZoologicoDAO.create_animal(animal)
        return idAnimalCriado

    #atualizando os dados
    def updateAnimal(self):
        id = input("Informe o id do animal a ser atualizado?")
        print("Entre com as informações a serem atualizadas")
        # inserindo os dados do cuidador
        idCuidador = input("Id cuidador: ")
        nomeCuidador = input("Nome cuidador: ")
        documentoCuidador = input("Documento cuidador: ")
        cuidador = Cuidador(idCuidador, nomeCuidador, documentoCuidador)

        # inserindo os dados do habitat
        idHabitat = input("Id habitat: ")
        nomeHabitat = input("Nome habitat: ")
        tipoAmbienteHabitat = input("Tipo habitat: ")
        habitat = Habitat(idHabitat, nomeHabitat, tipoAmbienteHabitat, cuidador)

        # inserindo os dados do animal
        idAnimal = input("Id animal: ")
        nomeAnimal = input("Nome animal: ")
        especieAnimal = input("Especie animal: ")
        idadeAnimal = input("Idade animal: ")
        animal = Animal(idAnimal, nomeAnimal, especieAnimal, idadeAnimal, habitat)

        ZoologicoDAO.update_animal(id, animal)

    #realizando uma busca
    def readAnimal(self):
        id = input("Informe o id do animal a ser buscado?")
        ZoologicoDAO.read_animal_by_id(id)

    #deletando um animal
    def deleteAnimal(self):
        id = input("Informe o id do animal a ser excluido?")
        ZoologicoDAO.delete_animal(id)