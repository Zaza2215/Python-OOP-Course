class User:
    def __init__(self, name='test'):
        self._name = name

    @property
    def name(self):
        # Printing below is done during initialization
        print('Value was returned!')
        return self._name

    @name.setter
    def name(self, value):
        print('The attribute was changed!')
        self._name = value

    @name.deleter
    def name(self):
        print('The attribute was deleted')

