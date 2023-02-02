class User:
    args = {
        'version': 1,
        'flags': 2,
    }

    def __init__(self):
        self.__dict__ = self.args


if __name__ == '__main__':
    a = User()
    b = User()
    c = User()
    print(a.__dict__)  # {'version': 1, 'flags': 2}
    print(a.args)  # {'version': 1, 'flags': 2}
    a.args['version'] = 2
    print(a.args)  # {'version': 2, 'flags': 2}
    print(b.args)  # {'version': 2, 'flags': 2}
    print(User.args)  # {'version': 2, 'flags': 2}
