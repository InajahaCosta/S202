from database import Database
from teacher import TeacherCRUD
from query import RedeSocialDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.207.85.74:7687", "neo4j", "turpitude-squares-sessions")

teacher_db = TeacherCRUD(db)
redesocial_db = RedeSocialDatabase(db)

class RedeSocial:
    # Função para criar os nós de usuarios:
    @staticmethod
    def criar_usuarios():
        redesocial_db.createUser()

    # Função para criar os nós de postagens:
    @staticmethod
    def criar_postagens():
        redesocial_db.createPost()

    # Função para criar os relacionamentos "AMIGO":
    @staticmethod
    def criar_amizade():
        redesocial_db.createFriendship()

    # Função para criar os relacionamentos "POSTOU":
    @staticmethod
    def criar_postou():
        redesocial_db.createPosted()

    @staticmethod
    def oldestUser():
        oldest = redesocial_db.oldestUser()
        return oldest

    @staticmethod
    def count30():
        users30 = redesocial_db.count30()
        return users30

    @staticmethod
    def calculateAverage():
        media = redesocial_db.calculateAverage()
        return media

# Cria uma instância da Classe Social para realizar as consultas:
social = RedeSocial()

# Chama a função para criar nós:
social.criar_usuarios()
social.criar_postagens()

# Chama as funções para criar relacionamentos:
social.criar_amizade()
social.criar_postou()

#Questão 2 :

#Encontre o usuário mais velho.
oldest_user = social.oldestUser()
print("O usuário mais velho é:", oldest_user["nome_usuario"])

#Quantos usuários têm mais de 30 anos?
users30 = social.count30()
print("A quantidade de usuários com mais de 30 anos é:", users30)

#Qual é a média de idade dos usuários?
average= social.calculateAverage()
print("A média de idade dos usuários é:", average, "anos \n ")


#Questão 3:

#realizando a criação do professor
teacher_db.create("Chris Lima", 1956, "189.052.396-66")

#pesquisando pelo professor com nome "Chris Lima"
print(teacher_db.read("Chris Lima"))

#Atualizando o cpf do professor "Chris Lima"
teacher_db.update("Chris Lima", "162.052.777-77")

# Fechando a conexão
db.close()