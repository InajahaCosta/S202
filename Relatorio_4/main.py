from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

class ProductAnalyzer:

    # Primeira questão
    def totalClienteB(self):
        result = db.collection.aggregate([
            {"$match": {"cliente_id": "B"}},
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id","total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": 2, "total": {"$avg": "$total"}}}
        ])
        writeAJson(result, "totalClienteB")
        pass

    # Segunda questão
    def menosVendido(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])
        writeAJson(result, "menosVendido")
        pass

    # terceira questão
    def menosGastou(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"},"total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": 1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])
        writeAJson(result, "menosGastou")
        pass

    # Products sold with the quantity of two or more units:
    def listaProduto(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 2}}},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
        ])
        writeAJson(result, "listaProduto")
        pass


ProductAnalyzer.totalClienteB(db.collection)
ProductAnalyzer.menosVendido(db.collection)
ProductAnalyzer.menosGastou(db.collection)
ProductAnalyzer.listaProduto(db.collection)