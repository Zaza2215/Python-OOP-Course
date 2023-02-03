class Test:
    def __init__(self, array: list):
        self.array = array

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __delitem__(self, index):
        del self.array[index]
