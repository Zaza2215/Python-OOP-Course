class User:
    version = 1

    def __init__(self, name='name'):
        self.name = name

    @classmethod
    def set_name(cls, value):
        cls.version = value


if __name__ == '__main__':
    a = User()
    b = User()
    c = User()
    print('a.version:', a.version)
    a.version = 2
    print('change value version in a')
    print('a.version:', a.version)
    print('b.version:', b.version)
    a.set_name(3)
    print('Use set name from a')
    print('a.version:', a.version)
    print('b.version:', b.version)
    print('c.version:', c.version)

