class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_data(self):
        print(f'name: {self.name}\nage: {self.age}')


a = User('Alex', 10)
b = User('John', 19)
