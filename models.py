from pydantic import BaseModel


class Path(BaseModel):
    name: str
    surname: str


class Queury(BaseModel):
    name: str
    surname: str


class Fullname(BaseModel):
    name: str
    surname: str
    age: int


class Birth(BaseModel):
    fullname: Fullname
    date: int
