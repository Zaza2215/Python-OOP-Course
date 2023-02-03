class Test:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __eq__(self, other):
        if other == self.value:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.value)


class P:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return 100

    def __sub__(self, other):
        return 100

    def __eq__(self, other):
        return self.value == other

    def __mul__(self, other):
        return self.value * other

    def __hash__(self):
        sh = hash(self)
        print('self.__hash__:', sh)
        return sh
