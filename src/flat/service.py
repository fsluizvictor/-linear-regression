from flat import repository
from flat.models import MyClass


def get_object(uid: str) -> MyClass:
    obj = repository.get(uid)
    return __map_to_my_class__(obj)

def update_object(object: dict):
    repository.update(object)

def save_object(object: MyClass):
    repository.create(object.__dict__)

def delete_object(uid: str):
    repository.delete(uid)

def __map_to_my_class__(object: dict) -> MyClass:
    return MyClass(**obj)
