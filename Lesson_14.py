class User:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)

    def __bytes__(self):
        if isinstance(self.value, int):
            print('int -> bytes')
            return bytes(self.value)
        elif isinstance(self.value, str):
            print('str -> bytes')
            return self.value.encode()
        else:
            print('other -> bytes')
            return str(self.value).encode()

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)


# Practice 14.1-14.4
class P:
    def __bool__(self):
        return True

    def __bytes__(self):
        return bytes(1)

    def __float__(self):
        return 100.0

    def __int__(self):
        return 100


if __name__ == '__main__':
    a = User(8)
    print(bool(a))
    print(bytes(a))
    print(float(a))
    print(int(a))
    print(type(a))
