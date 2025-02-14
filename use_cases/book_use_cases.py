from typing import List
from domain.entities import Book
from domain.repositories import BookRepository

class GetAllBooksUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> List[Book]:
        return self.repository.get_all_books()

class CreateBookUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, title: str, author_id: int) -> Book:
        return self.repository.create_book(title, author_id)