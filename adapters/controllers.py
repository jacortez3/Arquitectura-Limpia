from fastapi import FastAPI, HTTPException, Depends
from adapters.serializers import AuthorCreateSerializer, BookCreateSerializer
from use_cases.author_use_cases import GetAllAuthorsUseCase, CreateAuthorUseCase
from use_cases.book_use_cases import GetAllBooksUseCase, CreateBookUseCase
from infrastructure.repositories import InMemoryAuthorRepository, InMemoryBookRepository
from infrastructure.database import InMemoryDatabase

# Crear una instancia de la base de datos en memoria
db = InMemoryDatabase()

# Crear instancias de los repositorios
author_repository = InMemoryAuthorRepository(db)
book_repository = InMemoryBookRepository(db)

app = FastAPI()

# Funciones para inyectar dependencias
def get_author_repository():
    return author_repository

def get_book_repository():
    return book_repository

@app.get("/authors")
def get_all_authors(repo=Depends(get_author_repository)):
    use_case = GetAllAuthorsUseCase(repo)
    return use_case.execute()

@app.post("/authors")
def create_author(author_data: AuthorCreateSerializer, repo=Depends(get_author_repository)):
    use_case = CreateAuthorUseCase(repo)
    return use_case.execute(author_data.name, author_data.email)

@app.get("/books")
def get_all_books(repo=Depends(get_book_repository)):
    use_case = GetAllBooksUseCase(repo)
    return use_case.execute()

@app.post("/books")
def create_book(book_data: BookCreateSerializer, repo=Depends(get_book_repository)):
    use_case = CreateBookUseCase(repo)
    return use_case.execute(book_data.title, book_data.author_id)