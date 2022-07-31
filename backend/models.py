from sqlite3 import Date
from datetime import datetime


class BaseModel:
    # created_at = Date()
    # updated_at = datetime.now()

    # created_by =
    # updated_by =

    class Meta:
        abstract = True


class User(BaseModel):
    def __init__(self,
                 _id: int,
                 _username: str,
                 _password: str,
                 _email: str,
                 _phone: str,
                 _firstname: str,
                 _lastname: str):
        pass


class ToDo(BaseModel):
    def __init__(self,
                 _title: str,
                 _description: str):
        pass


class Group(BaseModel):
    def __init__(self,
                 _id: int,
                 _name: int):
        pass
