# from fastapi import APIRouter
# from enum import Enum
#
# router = APIRouter()
#
#
# class EnumExampleQuery(str, Enum):
#     lipetsk = 'lipetsk'
#     moscow = 'moscow'
#     kazan = 'kazan'
#     vladivostok = 'vladivostok'
#
#
#
#
#
# db = [{'name': 'Ivan'}, {'name': 'John'}, {'name': 'Smith'}, {'name': 'Sergey'}, {'name': 'Jack'}, {'name': 'Denis'},
#       {'name': 'Svetlana'}, ]
#
#
# @router.get("/")
# def get_examples2(skip: int = 0, limit: int = 2):
#     return db[skip:skip + limit]
#
#
# @router.get("/hh")
# def get_examples3(name: str, age: int | None = None):
#     if age==None: age='no'
#     return {"name": name, "age": age}
#
#
# @router.get("/{query}")
# def get_example(query: EnumExampleQuery):
#     if query == EnumExampleQuery.lipetsk:
#         return "Now lipetsk get query"
#     if query == EnumExampleQuery.moscow:
#         return "Now moscow get query"
#     return query
