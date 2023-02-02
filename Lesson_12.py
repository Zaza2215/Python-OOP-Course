from functools import singledispatch


class User:
    @singledispatch
    def get_value(value):
        print('default:', value)

    @get_value.register(int)
    def _(value):
        print('int:', value)

    @get_value.register(str)
    def _(value):
        print('str:', value)


# Practice 12.1

class P:
    @singledispatch
    def get_number(value):
        pass

    @get_number.register(int)
    def _(value):
        return 100

    @get_number.register(str)
    def _(value):
        return '100'


if __name__ == '__main__':
    User.get_value(12.0)
    User.get_value(12)
    User.get_value('12')
