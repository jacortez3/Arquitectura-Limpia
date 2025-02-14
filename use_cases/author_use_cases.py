from typing import List
from domain.entities import Author
from domain.repositories import AuthorRepository

class GetAllAuthorsUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all_authors()

class CreateAuthorUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, name: str, email: str):
        return self.repository.create_author(name, email)