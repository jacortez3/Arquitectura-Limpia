from dataclasses import dataclass
from typing import List

@dataclass
class Author:
    id: int
    name: str
    email: str

@dataclass
class Book:
    id: int
    title: str
    author_id: int