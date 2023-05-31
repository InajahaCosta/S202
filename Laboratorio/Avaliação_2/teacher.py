class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    #crianção dos dados
    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (t:Teacher {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})"
        self.db.execute_query(query)

    #Pesquisa pelos dados
    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return[(result["name"], result["ano_nasc"], result["cpf"]) for result in results]

    #Deletando os dados
    def delete(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DELETE t"
        self.db.execute_query(query)

    #atualizandos os dados
    def update(self, name, newCpf):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) SET t.cpf = '{newCpf}'"
        self.db.execute_query(query)