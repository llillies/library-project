from models import Author, Book

new_author = Author.get(Author.name == 'Colleen Hoover')
book = Book.get(Book.title=="É Assim que Acaba")

book.author = new_author

book.save()
