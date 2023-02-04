import collections


class Test:
    def __getattr__(self, attr):
        print('The attribute isn\'t exist!')


class Base:
    _fields = []

    def __init__(self, *args):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Base):
    _fields = ['name', 'shares', 'price']


class Base2:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)


class Stock2(Base2):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


# --- SECOND PART ---


class TestDict(dict):
    def __setitem__(self, key, value):
        print('__setitem__')
        super().__setitem__(key, [value] * 3)


class TestUserDict(collections.UserDict):
    def __setitem__(self, key, value):
        print('__setitem__(u)')
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    def module_1():
        t = Test()
        t.attribute
        # output: The attribute isn't exist!

        # --- --- ---

        a = Stock(1, 2, 3, 4)
        print(a.__dict__)
        # output: {'name': 1, 'shares': 2, 'price': 3}
        a = Stock(1, 2, 3, 4)
        print(a.__dict__)
        # output: {'name': 1, 'shares': 2, 'price': 3}
        a = Stock(1, 2)
        print(a.__dict__)
        # output: {'name':1, 'shares':2}

        # --- --- ---

        b = Stock2(2)
        print(b.spam())
        # output: getting: spam
        # None
        print(b.x)
        # output: getting: x
        # 2
        print(b.__getattribute__('x'))
        # output: getting: __getattribute__
        # getting: x
        # 2


    def module_2():
        a = TestDict(one=1, two=2)
        print(a)
        a.update(three=3)
        print(a)
        a['three'] = 3
        print(a)
        b = TestUserDict(one=1, two=2)
        print(b)
        b.update(three=3)
        print(b)
        b['three'] = 3
        print(b)


    module_2()
