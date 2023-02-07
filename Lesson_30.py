import time


def start_handler():
    for i in range(5):
        print(f'handler: {i}')
        time.sleep(1)


class Monitor:
    def __init__(self, exc_obj):
        self.func = exc_obj
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.func()
        return self.func

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f'lead time: {end_time - self.start_time}')


if __name__ == '__main__':
    with Monitor(start_handler) as fn:
        pass
