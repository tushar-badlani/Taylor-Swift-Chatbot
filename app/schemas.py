from pydantic import BaseModel


class Query(BaseModel):
    query: str


class Response(BaseModel):
    answer: str