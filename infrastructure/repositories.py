from typing import List
from domain.entities import Author, Book
from domain.repositories import AuthorRepository, BookRepository
from infrastructure.database import InMemoryDatabase

class InMemoryAuthorRepository(AuthorRepository):
    def __init__(self, db: InMemoryDatabase):
        self.db = db

    def get_all_authors(self) -> List[Author]:
        return self.db.authors

    def get_author_by_id(self, author_id: int) -> Author:
        for author in self.db.authors:
            if author.id == author_id:
                return author
        raise ValueError("Author not found")

    def create_author(self, name: str, email: str) -> Author:
        author = Author(id=self.db.current_author_id, name=name, email=email)
        self.db.authors.append(author)
        self.db.current_author_id += 1
        return author

class InMemoryBookRepository(BookRepository):
    def __init__(self, db: InMemoryDatabase):
        self.db = db

    def get_all_books(self) -> List[Book]:
        return self.db.books

    def get_book_by_id(self, book_id: int) -> Book:
        for book in self.db.books:
            if book.id == book_id:
                return book
        raise ValueError("Book not found")

    def create_book(self, title: str, author_id: int) -> Book:
        book = Book(id=self.db.current_book_id, title=title, author_id=author_id)
        self.db.books.append(book)
        self.db.current_book_id += 1
        return book