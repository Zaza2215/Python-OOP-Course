class Base:
    def __init__(self, health=100):
        self.health = health

    @staticmethod
    def go_to():
        print('go_to')

    def get_damage(self):
        self.health -= 10
        print(f'health: {self.health}')

    def restore_health(self):
        self.health += 10
        print(f'health: {self.health}')


class Warrior(Base):
    def __init__(self, health=120):
        super().__init__(health)

    def get_damage(self):
        self.health -= 5
        print(f'health: {self.health}')


class Wizard(Base):
    def __init__(self, health=80):
        super().__init__(health)

    def restore_health(self):
        self.health += 20
        print(f'health: {self.health}')
