class RedeSocialDatabase:
    def __init__(self, database):
        self.db = database

    # Criando os nós dos usuários
    def createUser(self):
        usuarios = [
            {"nome": "Alice", "idade": 25, "labels": ["Usuario"]},
            {"nome": "Bob", "idade": 30, "labels": ["Usuario"]},
            {"nome": "Charlie", "idade": 35, "labels": ["Usuario"]},
            {"nome": "David", "idade": 40, "labels": ["Usuario"]},
            {"nome": "Eve", "idade": 45, "labels": ["Usuario"]}
        ]

        for usuario in usuarios:
            query = """
            CREATE (u:Usuario {nome: $nome, idade: $idade})
            SET u :%s
            """ % ":".join(usuario["labels"])
            parameters = {
                "nome": usuario["nome"],
                "idade": usuario["idade"]
            }
            self.db.execute_query(query, parameters)

    # Criando os nós das postagens
    def createPost(self):
        postagens = [
            {"titulo": "Observações do Amanhecer", "conteudo": "Conteúdo da Observações do Amanhecer",
             "labels": ["Postagem"]},
            {"titulo": "Memórias da Tarde", "conteudo": "Conteúdo da Memórias da Tarde", "labels": ["Postagem"]},
            {"titulo": "Segredos da Noite", "conteudo": "Segredos da Noite", "labels": ["Postagem"]}
        ]

        for postagem in postagens:
            query = """
              CREATE (p:Postagem {titulo: $titulo, conteudo: $conteudo})
              SET p :%s
              """ % ":".join(postagem["labels"])
            parameters = {
                "titulo": postagem["titulo"],
                "conteudo": postagem["conteudo"]
            }
            self.db.execute_query(query, parameters)

    # Criando os relacionamentos "AMIGO"
    def createFriendship(self):
        relacionamentos = [
            {"amigo1_nome": "Alice", "amigo2_nome": "Bob"},
            {"amigo1_nome": "Bob", "amigo2_nome": "Charlie"},
            {"amigo1_nome": "Charlie", "amigo2_nome": "David"},
            {"amigo1_nome": "David", "amigo2_nome": "Eve"}
        ]

        for relacionamento in relacionamentos:
            query = """
               MATCH (amigo1:Usuario {nome: $amigo1_nome}), (amigo2:Usuario {nome: $amigo2_nome})
               CREATE (amigo1)-[:AMIGO]->(amigo2)
               """
            parameters = {
                "amigo1_nome": relacionamento["amigo1_nome"],
                "amigo2_nome": relacionamento["amigo2_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "POSTOU" com base nos dados fornecidos:
    def createPosted(self):
        relacionamentos = [
            {"usuario_nome": "Alice", "titulo": "Observações do Amanhecer"},
            {"usuario_nome": "Bob", "titulo": "Memórias da Tarde"},
            {"usuario_nome": "Charlie", "titulo": "Segredos da Noite"}
        ]

        for relacionamento in relacionamentos:
            query = """
                    MATCH (usuario:Usuario {nome: $usuario_nome}), (postagem:Postagem {titulo: $titulo})
                    CREATE (usuario)-[:POSTOU]->(postagem)
                    """
            parameters = {
                "usuario_nome": relacionamento["usuario_nome"],
                "titulo": relacionamento["titulo"],
            }
            self.db.execute_query(query, parameters)


    # Para encontra o usuário mais velho
    def oldestUser(self):
        query = """ MATCH (usuario:Usuario) RETURN usuario.nome AS nome_usuario, usuario.idade AS idade 
        ORDER BY idade DESC LIMIT 1 """
        result = self.db.execute_query(query)
        user = result[0]
        return user

    # realiza a conta de quantos usuários têm mais de 30 anos
    def count30(self):
        query = """ MATCH (usuario:Usuario) WHERE usuario.idade > 30 RETURN COUNT(usuario) AS total """
        result = self.db.execute_query(query)
        count = result[0]["total"]
        return count

    # Calcula a média de idade dos usuários
    def calculateAverage(self):
        query = """
        MATCH (usuario:Usuario) RETURN toInteger(AVG(usuario.idade)) AS media_idade """
        result = self.db.execute_query(query)
        average = result[0]["media_idade"]
        return average