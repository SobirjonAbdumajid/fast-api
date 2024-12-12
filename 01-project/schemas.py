from datetime import datetime

from pydantic import BaseModel

class Posts(BaseModel):
    name: str
    age: int
    birth_date: datetime
    enrollment_year: int








# from datetime import datetime
#
# from fastapi import FastAPI
# from sqlalchemy import MetaData, Table, insert, Column, Integer, String, create_engine
# from pydantic import BaseModel
# from typing import List, Union, Set
#
# engine = create_engine('postgresql+psycopg2://postgres:onamotam@localhost:5432/main_task_database')
# metadata_obj = MetaData()
# computers = Table("students", metadata_obj, autoload_with=engine)
#
# class ColumnIn(BaseModel):
#     name: Union[str, None] = None
#     age : Union[int, None] = None
#     birth_date: Union[datetime, None] = None
#     enrollment_year: Union[int, None] = None
# # name='John', age=244, birth_date="2023-01-01", enrollment_year=2005
# class ItemIn(BaseModel):
#     db_name: Union[str, None] = None
#     table_name: Union[str, None] = None
#     other: List[ColumnIn]
#
# app = FastAPI()
#
# @app.post("/computers/")
# async def create_computer(item: ItemIn):
#     try:
#         with engine.connect() as conn:
#             result = conn.execute(
#                 insert(computers),
#                 [ val for val in item.other])
#             conn.commit()
#             return item
#     except Exception as e:
#         print(e)
#         return item