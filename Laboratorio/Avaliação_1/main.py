from database import Database
from ZoologicoDAO import ZoologicoDAO

db = Database(database="animais", collection="animais")
db.resetDatabase()
zoologicoDAO = ZoologicoDAO(db)