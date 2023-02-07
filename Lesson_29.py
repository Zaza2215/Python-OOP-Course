def get_version():
    return 1


cls_dict = {
    'version': get_version,
    'name': 'Pasha',
    'age': 20
}

new_cls = type('Test', (), cls_dict)


class NoInstances(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError('Unable to instantiate')


class TestNoInstances(metaclass=NoInstances):
    @staticmethod
    def test():
        print('test')


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        print('Singleton initialization!')
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class TestSingleton(metaclass=Singleton):
    def __init__(self):
        print('Test created!')


if __name__ == '__main__':
    def fun_1():
        b = type('Test2', (), {})  # Create class
        print(b)
        c = b()  # Instantiation
        print(f'{c}\n')

    def fun_2():
        print(new_cls)
        print(vars(new_cls))
        print(f'{new_cls.version()}, {new_cls.name}, {new_cls.age}\n')

    def fun_3():
        try:
            a = TestNoInstances()
        except TypeError as ex:
            print(ex)

        TestNoInstances.test()
        print()

    # s = TestSingleton()
    # print(s)
    # s2 = TestSingleton()
    # print(s2)
    a = TestSingleton()
    print(a)
