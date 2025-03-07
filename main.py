import json
import os
from fastapi import FastAPI


app = FastAPI()

Books_file = "books.json"

Books = [
    "Harry Potter",
    "The Lord of the Rings",
    "The Little Prince",
    "The Da Vinci Code",
    "The Alchemist",
    "The Catcher in the Rye",
    "The Hunger Games"
]

if os.path.exists(Books_file):
    with open(Books_file, "r") as file:
        Books = json.load(file)
    

@app.get("/")
async def root():
    return {"message": "This is the main page"}

# /list-books -> rota para mostrar os livros cadastrados
@app.get("/list-books")
async def list_books():
    return {f"Books": Books}

# /list-book-by-index -> rota para mostrar um livro específico
@app.get("/list-book-by-index/{index}")
async def list_book_by_index(index: int):
    if index >= len(Books):
        return {"message": "Index out of range"}
    return {"Books": Books[index]}

# /get-randoom-book -> rota para mostrar um livro aleatório
@app.get("/get-random-book")
async def get_random_book():
    import random
    return random.choice(Books)

# /add-book -> rota para adicionar um livro
@app.post("/add-book")
async def add_book(book: str):
    Books.append(book)
    with open(Books_file, "w") as file:
        json.dump(Books, file)
    return {f"The {book} book was added.": Books}

