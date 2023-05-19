from database import Database
from game_database import gameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.210.246.73:7687", "neo4j", "knob-discretion-mondays")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = gameDatabase(db)


#criando os jogadores
game_db.create_player("Rafael", 25)
game_db.create_player("Maria", 38)
game_db.create_player("Joao", 43)
game_db.create_player("Sophia", 53)

#criando os jogos
game_db.create_match("Rafael", 25, "Maria", 38, 1, 10)
game_db.create_match("Joao", 43, "Sophia", 53, 2, 15)

#exibindo
print(game_db.get_player())
print(game_db.get_match())


#atualizando
game_db.update_player("Rafael", "Junior", 25)
print(game_db.get_player())

#deletando
game_db.delete_player("Sophia", 53)
print(game_db.get_player())

# Fechando a conexão
db.close()