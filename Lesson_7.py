class User:
    # attribute __slots__ isn't inherited
    __slots__ = ['name', 'age']

    def __init__(self, name='name', age=20):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)


if __name__ == '__main__':
    a = User()
    # print(User.__dict__)
    # print(a.__dict__)
    b = User()
    # a.data = 2
    # b.data = 1
