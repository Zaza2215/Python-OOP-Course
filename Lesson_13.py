class User:
    def __init__(self, value='test'):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'<{self.value} {hex(id(self.value))} object>'

    def __del__(self):
        print('The class instance has been deleted')


# Practice 13.1-13.3

class P:
    def __len__(self):
        return 100

    def __str__(self):
        return '100'

    def __repr__(self):
        return f'self: {self}'

    def __del__(self):
        print('Wow, I has been deleted')


if __name__ == '__main__':

    def check(a):
        print(len(a))
        print(str(a))
        print(repr(a))
        del a

    a = User()
    check(a)
    a = P()
    check(a)
