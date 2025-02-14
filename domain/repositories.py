from abc import ABC, abstractmethod
from typing import List
from domain.entities import Author, Book

class AuthorRepository(ABC):
    @abstractmethod
    def get_all_authors(self) -> List[Author]:
        pass

    @abstractmethod
    def get_author_by_id(self, author_id: int) -> Author:
        pass

    @abstractmethod
    def create_author(self, name: str, email: str) -> Author:
        pass

class BookRepository(ABC):
    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def get_book_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def create_book(self, title: str, author_id: int) -> Book:
        pass