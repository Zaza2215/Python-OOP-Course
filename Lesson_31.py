import time


class Monitor:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        self.start = time.time()
        self.fun()
        self.end = time.time()
        print(f'Duration: {self.end - self.start}')


@Monitor
def start_handler():
    for i in range(5):
        print(f'handler: {i}')
        time.sleep(1)


class Test:
    def __init__(self, name='Pasha'):
        self.name = name

    @Monitor
    def test(self):
        for i in range(len(self.name)):
            print(i)
            time.sleep(1)


if __name__ == '__main__':
    start_handler()
    # Test.test()  # It doesn't work with
