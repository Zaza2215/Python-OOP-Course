class Info:
    version = '1.0'

    def get_version(self):
        return self.version


# --- --- ---

class Test:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def get():
        print('Test')


class Test2:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get():
        print('Test2')


class Template(Test, Test2):
    def __init__(self, name, age):
        Test.__init__(self, age)
        Test2.__init__(self, name)

    @staticmethod
    def start():
        Test.get()
        Test2.get()


if __name__ == '__main__':
    print(vars(Info))
    for key in vars(Info):
        attr_value = vars(Info)[key]
        print(f'{key}: {callable(attr_value)}')

    print('--- --- ---')

    print(Template.mro())
    Template.get()
    Template.start()

    a = Template('Pasha', 20)
    print(a.age)
    print(a.name)
