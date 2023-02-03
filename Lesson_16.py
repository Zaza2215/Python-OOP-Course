class User:
    def __init__(self, value):
        self.value = value

    def __call__(self, comment):
        print('__call__:', self.value)
        print('comment:', comment)

    def __iter__(self, other=0):
        print('__iter__')
        # if not ('array' in self.__dict__.keys()) or not self.array:
        # UPDATE
        if not hasattr(self, 'array') or not self.array:
            self.array = [i for i in range(other, 0, -1)]
        return self

    def __next__(self):
        if self.array:
            return f'__next__: {self.array.pop()}'
        else:
            raise StopIteration('self.array is empty')


if __name__ == '__main__':
    a = User(12)
    a('Hello')
    b = a.__iter__(5)
    for i in b:
        print(i)
