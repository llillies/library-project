import peewee

db = peewee.SqliteDatabase('codigo_avulso.db')


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        database = db

class Author(BaseModel):
    """
    Classe que representa a tabela Author
    """
    name = peewee.CharField(unique=True)

class Book(BaseModel):
    """
    Classe que representa a tabela Book
    """

    title = peewee.CharField(unique=True)

    author = peewee.ForeignKeyField(Author)

if __name__ == '__main__':
    try:
        Author.create_table()
        print("Tabela 'Author' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Author' ja existe!")

    try:
        Book.create_table()
        print("Tabela 'Book' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Book' ja existe!")

