from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.reset_database()
pokemons = db.collection.find()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

#pegando somente as informações do pokemon Venusaur id 3
Venusaur = getPokemonByDex(3)
writeAJson(Venusaur, "Venusaur")

#pegando por tipo Grass e ataque menor igual á 40
pokemon = db.collection.find({"type": "Grass", "base.Attack": { "$lte": 40 }})
writeAJson(pokemon, "pokemon_grass")

#pegando por tipo Steel e ataque menor igual á 80
pokemon = db.collection.find({"type": "Steel", "base.Attack": { "$lte": 80 }})
writeAJson(pokemon, "pokemon_steel")

#pegando por tipo Fire e HP maior que  60
pokemon = db.collection.find({"type": "Fire", "base.HP": { "$gte": 60 }})
writeAJson(pokemon, "pokemon_fire")

#pegando os com o nome com 7 ou menos letras
def get_7_letters_or_less(collection):
  names = collection.find({}, {"name": 1})
  four_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 5:
      if all(len(word) <= 7 for word in name["name"].values()):
        four_letters_or_less.append(name["name"].values())
  return four_letters_or_less

writeAJson(get_7_letters_or_less(db.collection), "pokemon_7_words_or_less")
