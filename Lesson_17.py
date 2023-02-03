class User:
    def __init__(self):
        self.array = [1, 2, 3]

    def __enter__(self):
        print('__enter__')
        return self.array

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        del self.array


class File:
    def __init__(self, filename, flag='r'):
        self.file = open(filename, flag)

    def __enter__(self):
        print('__enter__')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.file.close()


# region interesting with singledispatch
# It doesn't work
# from functools import singledispatch
#
#
# class A:
#     def __init__(self, value):
#         self.value = value
#
#     @singledispatch
#     def get_value(self):
#         print('other')
#         return self.value
#
#     @get_value.register(int)
#     def _(self):
#         print('int')
#         return self.value
#
#     @get_value.register(str)
#     def _(self):
#         print('str')
#         return self.value
# endregion

if __name__ == '__main__':
    print()
    a = User()
    with a as arr:
        print(arr[0])

    with File('test.txt', 'w') as file:
        file.write('Hello, world!')

    with File('test.txt') as file:
        result = file.read()
        print(result)
