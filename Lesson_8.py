class Test:
    def __new__(cls, *args, **kwargs):
        print('Creating an instance of a class')
        instance = super().__new__(cls)
        # for more old versions
        # instance = super(Test, cls).__new__(cls)
        return instance

    def __init__(self, name):
        print('Initialization')
        self.name = name


if __name__ == '__main__':
    # To skip initialization
    a = Test.__new__(Test)
