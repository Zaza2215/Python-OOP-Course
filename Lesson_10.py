class Public:
    def __init__(self, name='name'):
        self.name = name


class Private:
    def __init__(self, name='name'):
        self._name = name


class Protected:
    def __init__(self, name='name'):
        self.__name = name


class ProtectedWithSlots:
    __slots__ = ['__name']

    def __init__(self, name='name'):
        self.__name = name
