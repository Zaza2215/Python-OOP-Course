from sys import getsizeof
from Lesson_21 import *

wz1 = Wizard()
b1 = Base()
# print(issubclass(wz1, Base)) # TypeError
print(issubclass(Wizard, Base))  # True
print('Wizard class:', getsizeof(Wizard))  # 1072
print('wz1:', getsizeof(wz1))  # 48
print('Base class:', getsizeof(Base))  # 1072
print('b1:', getsizeof(b1))  # 48
print(isinstance(wz1, Wizard))  # True
print(isinstance(wz1, Base))  # True
print(isinstance(b1, Wizard))  # False
