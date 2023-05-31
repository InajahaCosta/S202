class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    # Cria nós com base nos dados fornecidos:
    def criar_nos_pessoas(self):
        pessoas = [
            {"nome": "Rafael", "sexo": "M", "idade": 30, "labels": ["Pessoa", "Carteiro"]},
            {"nome": "Inajaha", "sexo": "F", "idade": 27, "labels": ["Pessoa", "Engenheira"]},
            {"nome": "Maria Luisa", "sexo": "F", "idade": 6, "labels": ["Pessoa", "Criança"]},
            {"nome": "Daniel", "sexo": "M", "idade": 23, "labels": ["Pessoa", "Montador"]},
            {"nome": "Nayara", "sexo": "F", "idade": 22, "labels": ["Pessoa", "Secretaria"]},
            {"nome": "Sophia", "sexo": "F", "idade": 4, "labels": ["Pessoa", "Criança"]},
            {"nome": "Carlos", "sexo": "M", "idade": 58, "labels": ["Pessoa", "Mecanico"]},
            {"nome": "Eni", "sexo": "F", "idade": 56, "labels": ["Pessoa", "Montadora"]},
            {"nome": "Tabata", "sexo": "F", "idade": 27, "labels": ["Pessoa", "Fisioterapelta"]},
            {"nome": "Dayse", "sexo": "F", "idade": 18, "labels": ["Pessoa", "Engenheira"]},
            {"nome": "Patrick", "sexo": "M", "idade": 27, "labels": ["Pessoa", "Tecnico"]},
        ]

        for pessoa in pessoas:
            query = """
            CREATE (p:Pessoa {nome: $nome, sexo: $sexo, idade: $idade})
            SET p :%s
            """ % ":".join(pessoa["labels"])
            parameters = {
                "nome": pessoa["nome"],
                "sexo": pessoa["sexo"],
                "idade": pessoa["idade"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "PAI_DE" com base nos dados fornecidos:
    def criar_relacionamentos_pai_de(self):
        relacionamentos = [
            {"pai_nome": "Rafael", "filho_nome": "Maria Luisa"},
            {"pai_nome": "Daniel", "filho_nome": "Sophia"},
            {"pai_nome": "Carlos", "filho_nome": "Inajaha"},
            {"pai_nome": "Carlos", "filho_nome": "Nayara"},
        ]

        for relacionamento in relacionamentos:
            query = """
               MATCH (pai:Pessoa {nome: $pai_nome}), (filho:Pessoa {nome: $filho_nome})
               CREATE (pai)-[:PAI_DE]->(filho)
               """
            parameters = {
                "pai_nome": relacionamento["pai_nome"],
                "filho_nome": relacionamento["filho_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "ESPOSO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_esposo_de(self):
        relacionamentos = [
            {"marido_nome": "Rafael", "esposa_nome": "Inajaha"},
            {"marido_nome": "Carlos", "esposa_nome": "Eni"}
        ]

        for relacionamento in relacionamentos:
            query = """
                    MATCH (marido:Pessoa {nome: $marido_nome}), (esposa:Pessoa {nome: $esposa_nome})
                    CREATE (marido)-[:ESPOSO_DE]->(esposa)
                    """
            parameters = {
                "marido_nome": relacionamento["marido_nome"],
                "esposa_nome": relacionamento["esposa_nome"],
            }
            self.db.execute_query(query, parameters)


    # Cria relacionamentos "IRMAO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_irmao_de(self):
        relacionamentos = [
            {"irmao1_nome": "Nayara", "irmao2_nome": "Inajaha"},
        ]

        for relacionamento in relacionamentos:
            query = """
                MATCH (irmao1:Pessoa {nome: $irmao1_nome}), (irmao2:Pessoa {nome: $irmao2_nome})
                CREATE (irmao1)-[:IRMAO_DE]->(irmao2)
                """
            parameters = {
                "irmao1_nome": relacionamento["irmao1_nome"],
                "irmao2_nome": relacionamento["irmao2_nome"]
            }
            self.db.execute_query(query, parameters)
    def criar_relacionamentos_namorado_de(self): #criando relacionamento namorado_de
        relacionamentos = [
            {"namorado1_nome": "Daniel", "namorado2_nome": "Nayara"},
        ]
        for relacionamento in relacionamentos:
            query = """
                        MATCH (namorado1:Pessoa {nome: $namorado1_nome}), (namorado2:Pessoa {nome: $namorado2_nome})
                        CREATE (namorado1)-[:NAMORADO_DE]->(namorado2)
                        """
            parameters = {
                "namorado1_nome": relacionamento["namorado1_nome"],
                "namorado2_nome": relacionamento["namorado2_nome"]
            }
            self.db.execute_query(query, parameters)



    #Realizando as consultas
    def get_namorado(self, namorado2_nome):
        query = """
             MATCH (namorado2:Pessoa {nome: $namorado2_nome})<-[:NAMORADO_DE]-(namorado1:Pessoa)
             RETURN namorado1.nome AS nome
             """
        parameters = {"namorado2_nome": namorado2_nome}
        results = self.db.execute_query(query, parameters)
        return results

    def get_filhos(self, pai_nome):
        query = """
            MATCH (pai:Pessoa {nome: $pai_nome})-[:PAI_DE]->(filho:Pessoa)
            RETURN filho.nome AS nome
            """
        parameters = {"pai_nome": pai_nome}
        results = self.db.execute_query(query, parameters)
        return results

    def get_irmaos(self, irmao1):
        query = """
            MATCH (irmao1:Pessoa {nome: $irmao1_nome})-[:IRMAO_DE]->(irmao2:Pessoa)
            RETURN irmao2.nome AS nome
            """
        parameters = {"irmao1_nome": irmao1_nome}
        results = self.db.execute_query(query, parameters)
        return results