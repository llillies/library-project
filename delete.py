from models import Author, Book

book = Book.get(Book.title=="Persuasão")

book.delete_instance()
