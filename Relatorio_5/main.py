from database import Database
from model import BookModel

db = Database(database="relatorio5", collection="livros")
db.resetDatabase()
book_model = BookModel(db)

# Create book:
id_book01 = book_model.create_book("Moby Dick", "Herman Melville", 1851, 25.0)
id_book02 = book_model.create_book("1984", "George Orwell", 1949, 20.0)

# Read book:
book1 = book_model.read_book_by_id(id_book01)
book2 = book_model.read_book_by_id(id_book02)

# Update book:
book_model.update_book(id_book01, "O Agir de Deus", "Luciano Subira", 40.0)
book_model.update_book(id_book02, "O Milagre do Amanha", "Hal Elrod", 20.0)

# Read book:
book_1 = book_model.read_book_by_id(id_book01)
book_2 = book_model.read_book_by_id(id_book02)

# Delete book:
book_model.delete_book(id_book01)
book_model.delete_book(id_book02)