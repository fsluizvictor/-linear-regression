from dataclasses import dataclass
from datetime import datetime
import typing

T = typing.TypeVar('T')

class HasRepositoryInterface(typing.Protocol):
    def get(uid: str): ...
    def delete(uid: str): ...
    def update(obj: T): ...
    def create(obj: T): ...



@dataclass
class MyClass:
    uid: str
    createdAt: datetime
    modifiedAt: datetime
