from models import Author, Book

author_1 = Author.create(name='Jane Austen')

author_2 = Author.create(name='Karen M. McManus')

book_1 = {
    'title': 'Orgulho e preconceito',
    'author_id': author_1,
}

book_2 = {
    'title': 'Um de nós está mentindo',
    'author_id': author_2,
}

book_3 = {
    'title': 'Os primos',
    'author_id': author_2,
}

book_4 = {
    'title': 'Persuasão',
    'author_id': author_1,
}

books = [book_1, book_2, book_3, book_4]

Book.insert_many(books).execute()
