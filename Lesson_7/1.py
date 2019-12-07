"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

array = [random.randint(-100, 99) for _ in range(10)]
print(array)


def sort_bubble(array):

    for i in range(len(array) - 1):
        action = False
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                action = True
        if not action:
            break
    return array


print(sort_bubble(array))
