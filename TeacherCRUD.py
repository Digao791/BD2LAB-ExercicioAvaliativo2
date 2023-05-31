
class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def createNode(self, name, ano_nasc, cpf):
        query = "CREATE (:Professor {name:" + '"' + f"{name}" + '"' + ", ano_nasc:" +  f"{ano_nasc}, cpf:" + '"' +  f"{cpf}" + '"' + "})"
        print(query)
        self.db.execute_query(query)

    def readNode(self, name:str):
        query = f"MATCH (p:Professor) where p.name = " + '"' + f"{name}" + '"' + " RETURN p.name AS nome, p.ano_nasc AS ano, p.cpf AS cpf "
        print(query)
        results = self.db.execute_query(query)
        return [(result['nome'], result['ano'], result['cpf']) for result in results]

    def deleteNode(self, name):
        query = "MATCH (p:Professor {name:" + '"' + f"{name}" + '"' + "}) DETACH DELETE p"
        print(query)
        self.db.execute_query(query)

    def updateNode(self, name, new_cpf):
        query = "MATCH (p:Professor {name:" + '"' + f"{name}" + '"}' + f") SET p.cpf = " + '"' + f"{new_cpf}" + '"'
        print(query)
        self.db.execute_query(query)
