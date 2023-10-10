from fastapi import FastAPI
from models import *
from wikipedia import *

app = FastAPI()


@app.get("/{name}/{surname}")
def with_path(name: str, surname: str):
    n = Path(name=name, surname=surname)
    return n, wikipedia.search(n)


@app.get("/query")
def with_query(name: str, surname: str):
    m = Queury(name=name, surname=surname)
    return m, wikipedia.search(m)


@app.post("/cls")
def with_class(fullname: Fullname):
    b = Birth(fullname=fullname, date=2023 - fullname.age)
    return b, wikipedia.search(b)
