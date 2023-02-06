class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

    @staticmethod
    def test():
        print('test')


@Counter  # printer = Counter(printer)
def printer():
    print('printer')


@Counter  # new = Counter(new)
def new():
    print('new')


def my_dec(fun):
    def inner(*args, **kwargs):
        print('Into my decorator: ', end='')
        return fun(*args, **kwargs)

    return inner


@my_dec  # old = my_dec(old)(*args, **kwargs)
def old():
    print('old')


def my_dec2(parameter_1):
    def inner(fun):
        def inner_2(*args, **kwargs):
            print(f'My decorator with parameters: parameter_1 = {parameter_1} fun: ', end='')
            return fun(*args, **kwargs)

        return inner_2

    return inner


@my_dec2(8)  # func = my_dec2(8)(func)(*args, **kwargs)
def func():
    print('func')


if __name__ == '__main__':
    printer()
    printer()
    printer()
    print(printer.count)
    Counter.test()
    print(printer.count)
    printer.test()
    print(printer.count)
    print(new.count)
    new()
    print(new.count)
    old()
    func()
