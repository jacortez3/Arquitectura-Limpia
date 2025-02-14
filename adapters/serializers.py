from pydantic import BaseModel

class AuthorCreateSerializer(BaseModel):
    name: str
    email: str

class BookCreateSerializer(BaseModel):
    title: str
    author_id: int