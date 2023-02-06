from abc import ABCMeta, abstractmethod


class Users(metaclass=ABCMeta):
    @abstractmethod
    def go_to(self):
        pass

    @abstractmethod
    def read(self):
        pass


class Test1(object):
    pass


class Test2(Users):
    pass


class Test3(Users):
    def go_to(self):
        pass

    def read(self):
        pass


if __name__ == '__main__':

    def exception_handler(cls_object):
        try:
            obj = cls_object()
            print(f'{cls_object.__name__} is good')
            return obj
        except Exception as ex:
            print(ex)

    list_of_classes = [Users, Test1, Test2, Test3]
    for cls in list_of_classes:
        exception_handler(cls)
