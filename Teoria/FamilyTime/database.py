from neo4j import GraphDatabase

class Database:
    # Inicializa a conexão com o banco de dados Neo4j, utilizando as informações de URI, usuário e senha fornecidas:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print("\nDatabase successfully connected!\n")

    # Encerra a conexão com o banco de dados
    def close(self):
        self.driver.close()

    # Executa uma consulta Cypher no banco de dados, com a consulta e os parâmetros fornecidos:
    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)  # Coleta os registros de resultado da consulta

            return data

    # Executa uma consulta Cypher para excluir todos os nós e relacionamentos do banco de dados:
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")