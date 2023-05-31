from Database import Database
from TeacherCRUD import TeacherCRUD


db = Database("bolt://localhost:7687", "neo4j", "Rainbowsix791")

base = TeacherCRUD(db)

base.createNode("Chris Lima", 1956, "189.052.396.66")

print(base.readNode("Chris Lima"))

base.updateNode("Chris Lima", "162.052.777-77")

db.close()