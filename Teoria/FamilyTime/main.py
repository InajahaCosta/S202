from database import Database
from query import FamilyDatabase

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j:
db = Database("bolt://3.94.149.233:7687", "neo4j", "speeders-leads-superstructure")
db.drop_all()

# Cria uma instância da classe FamilyDatabase para interagir com o banco de dados:
family_db = FamilyDatabase(db)


class Family:
    # Função para criar os nós de pessoas:
    @staticmethod
    def criar_nos_pessoas():
        family_db.criar_nos_pessoas()

    # Função para criar os relacionamentos "PAI_DE":
    @staticmethod
    def criar_relacionamentos_pai_de():
        family_db.criar_relacionamentos_pai_de()

    # Função para criar os relacionamentos "ESPOSO_DE":
    @staticmethod
    def criar_relacionamentos_esposo_de():
        family_db.criar_relacionamentos_esposo_de()

    # Função para criar os relacionamentos "IRMAO_DE":
    @staticmethod
    def criar_relacionamentos_irmao_de():
        family_db.criar_relacionamentos_irmao_de()

    # Função para criar os relacionamentos "NAMORADO_DE":
    @staticmethod
    def criar_relacionamentos_namorado_de():
        family_db.criar_relacionamentos_namorado_de()


    # Chama o método getNamorado da classe FamilyDatabase:
    @staticmethod
    def getNamorado(namorado2_nome):
        nome_namorado1 = family_db.get_namorado(namorado2_nome)
        return nome_namorado1

    # Chama o método getFilhos da classe FamilyDatabase:
    @staticmethod
    def getFilhos(pai_nome):
        nome_Filhos = family_db.get_filhos(pai_nome)
        return nome_Filhos

    # Chama o método getIrmaos da classe FamilyDatabase:
    @staticmethod
    def getIrmaos(irmao1):
        nome_irmaos = family_db.get_irmaos(irmao1)
        return nome_irmaos

# Cria uma instância da Classe Family para realizar as consultas:
family = Family()

# Chama a função para criar nós:
family.criar_nos_pessoas()

# Chama as funções para criar relacionamentos:
family.criar_relacionamentos_pai_de()
family.criar_relacionamentos_esposo_de()
family.criar_relacionamentos_irmao_de()
family.criar_relacionamentos_namorado_de()



#Saindo com o valor das consultas
namorado = family.getNamorado("Daniel")
print("A namorado de Daniel é:", namorado)

filho = family.getFilhos("Carlos")
print("Os filhos de Carlos são:", filho)

irmao = family.getIrmaos("Inajaha")
print("Inajaha e irma de:", irmao)
