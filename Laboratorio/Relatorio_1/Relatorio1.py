class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)
    def muda_cor(self, nova_cor):
        self.cor = nova_cor

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.som)
    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        print(novo_tamanho)

som = str("Pah")
nome = input("Entre com o nome do elefante: ")
idade = int(input("Entre com a idade do elefante: "))
especie = input("Entre com a especie do elefante: ")
cor = input("Entre coma cor do elefante: ")
tamanho = input("Entre com o tamanho do elefante: ")

if especie == "Africano" and idade < 10:
    tamanho = "pequeno"
    som = "Paaah"
elif especie == "Africano" and idade >= 10:
    tamanho = "grande"
    som = "PAHHHHHH"

elefantes = Elefante(nome, idade, especie, cor, som, tamanho)
elefantes.trombar()
elefantes.mudar_tamanho(tamanho)

