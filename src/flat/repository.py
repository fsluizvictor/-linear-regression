from db import DbClient


db_client = DbClient("url")


def get(uid: str) -> dict:
    ...

def update(object: dict):
    ...

def delete(uid: str):
    ...

def create(object: dict):
    ...
