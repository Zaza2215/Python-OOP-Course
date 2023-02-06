class Test:
    def __init__(self):
        self.__dict__['age'] = 0


def get_version(self):
    return 22


Test.version = get_version

import sys


class ChangeMe:
    def __init__(self):
        local = sys._getframe(1).f_locals
        print(local)
        self.__dict__.update((key, value) for key, value in local.items() if callable(value))


def test1():
    print('test1')


def test2():
    print('test2')


def test3():
    print('test3')


if __name__ == '__main__':
    print(vars(Test))
    print(Test.version)
    Test.name = 'Pasha'
    print(vars(Test))
    a = Test()
    print(vars(a))
    print(a.version())
    print(a.age)
    # print(Test.age) #  error
    c = ChangeMe()
    c.test1()
    c.test2()
    c.test3()