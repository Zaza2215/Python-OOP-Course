from typing import Any
from dataclasses import dataclass


@dataclass
class User:
    name: str = 'name'
    age: int = 'age'
    flags: list = 'list'
    comment: Any = 'Any'


class Test(User):
    def get_name(self):
        return self.name


if __name__ == '__main__':
    a = User(name='Pasha', age=20, flags=[1, 2, 3], comment=True)
    print(a)
    print(a.name)
    b = Test()
    print(b)
    print(b.get_name())