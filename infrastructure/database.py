from typing import List
from domain.entities import Author, Book

# Simulación de una base de datos en memoria
class InMemoryDatabase:
    def __init__(self):
        self.authors = []
        self.books = []
        self.current_author_id = 1
        self.current_book_id = 1