"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof
from sys import getsizeof


class MakingToys:

    def __init__(
            self,
            name='demo_name',
            color='demo_color',
            toys_type='demo_toys_type'):
        self.name = name
        self.color = color
        self.toys_type = toys_type

    def purchase_of_raw_materials(self):
        print('Закупка сырья')

    def tailoring(self):
        print('Пошив')

    def coloring(self):
        print('Окраска')


class MakingToysSlot:
    __slots__ = ['name', 'color', 'toys_type']

    def __init__(
            self,
            name='demo_name',
            color='demo_color',
            toys_type='demo_toys_type'):
        self.name = name
        self.color = color
        self.toys_type = toys_type

    def purchase_of_raw_materials(self):
        print('Закупка сырья')

    def tailoring(self):
        print('Пошив')

    def coloring(self):
        print('Окраска')


toys = MakingToys('робот', 'красный', 'лего')
print(asizeof.asizeof(toys), getsizeof(toys))
toys_slot = MakingToysSlot('робот1', 'красный1', 'лего1')
print(asizeof.asizeof(toys_slot), getsizeof(toys_slot))


"""
Применение слотов экономит память почти в два раза, getsizeof не приминим для измерение памяти для сложных структур
"""