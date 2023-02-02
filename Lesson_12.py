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


if __name__ == '__main__':
    User.get_value(12.0)
    User.get_value(12)
    User.get_value('12')
