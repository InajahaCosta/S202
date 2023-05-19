class gameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, id):
        query = "CREATE (p:Player {name: $name, id: $id})"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)

    def create_match(self, name_player1, id_player1, name_player2, id_player2, id_match, score_match):
        query = "MATCH (p1:Player {name: $name_player1, id: $id_player1}) MATCH (p2:Player {name: $name_player2, id: $id_player2}) CREATE (m:Match {id: $idmatch, players: $players, score: $score}) CREATE (p1)-[:JOGOU]->(m) CREATE (p2)-[:JOGOU]->(m) "
        parameters = {"idmatch": id_match, "players": [name_player1, name_player2], "score": score_match,
                      "name_player1": name_player1, "id_player1": id_player1, "name_player2": name_player2,
                      "id_player2": id_player2}
        self.db.execute_query(query, parameters)

    def update_player(self, old_name, new_name, id):
        query = "MATCH (p:Player {name: $old_name, id: $id}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name, "id": id}
        self.db.execute_query(query, parameters)

    def get_player(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.id AS id"
        results = self.db.execute_query(query)
        return [(result["name"], result["id"]) for result in results]

    def get_match(self):
        query = "MATCH (m:Match) RETURN m.id AS id, m.players AS players, m.score AS score"
        results = self.db.execute_query(query)
        return [(result["id"], result["players"], result["score"]) for result in results]

    def delete_player(self, name, id):
        query = "MATCH (p:Player {name: $name, id: $id}) DETACH DELETE p"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)