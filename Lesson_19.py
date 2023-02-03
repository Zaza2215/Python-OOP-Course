# hasattr(), getattr()
class Test:
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    print(hasattr(Test, 'value'))
    a = Test(111)
    print(hasattr(Test, 'value'))
    print(hasattr(a, 'value'))
    print(getattr(Test, 'value', None))
