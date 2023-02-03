class Test:
    def __init__(self, array: dict):
        self.array = array

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __delitem__(self, index):
        del self.array[index]


a = Test({'name': 1, 'surname': 2})
print(a['name'])
del a['name']
print(a.array)
a['surname'] = 1
print(a.array)