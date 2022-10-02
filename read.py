from models import Author, Book

book = Book.get(Book.title == "Os primos").get()
print(book.title)

books = Book.select().join(Author).where(Author.name=='Jane Austen')

print(books.count())

for book in books:
    print(book.title)

