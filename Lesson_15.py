class User:
    def __init__(self, value):
        self.value = value
        self.array = [1, 2, 3]

    def __pow__(self, power, modulo=None):
        return self.value ** power

    def __reversed__(self):
        self.array.reverse()
        return self.array

    def __truediv__(self, other):
        return int(self.value / other)


if __name__ == '__main__':
    a = User(10)
    print(a ** 2)
    print(reversed(a))
    print(reversed(a))
    print(a / 2)
