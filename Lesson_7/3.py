"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random
import timeit

m = 30
n = 2 * m + 1
array = [random.randint(0, 9) for i in range(n)]


def median_sort(array):
    array_copy = sorted(array.copy())
    med = array_copy[len(array_copy) // 2]
    return med


def find_median(array):
    index = 0
    min = len(array)
    unique_dict = {}
    for i in range(len(array)):
        if not unique_dict.setdefault(array[i]):
            unique_dict[array[i]] = i
            count_right = 0
            count_left = 0
            count = 0
            for j in range(len(array)):
                if i != j:
                    if array[i] < array[j]:
                        count_right += 1
                    elif array[i] > array[j]:
                        count_left += 1
                    else:
                        count += 1
            # print(array[i], count_right, count_left, count)
            if count_left == len(array) // 2 or count_right == len(array) // 2 or count == len(
                    array) or count_left == count_right or abs(count_left - count_right) == count:
                return array[i]
            if min > abs(abs(count_left - count_right) - count):
                min = abs(abs(count_left - count_right) - count)
                index = i
    return array[index]


# array = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9]


# for i in range(10000):
#     array = [random.randint(0, 9) for i in range(n)]
#     med_1 = median_sort(array)
#     med_2 = find_median(array)
#     # print('№', i, med_1, med_2)
#     if med_1 != med_2:
#         print('№', i, med_1, med_2)
#         print(array.sort())
#         break
print(
    timeit.timeit(
        "median_sort(array)",
        setup="from __main__ import median_sort, array",
        number=1000))
print(
    timeit.timeit(
        "find_median(array)",
        setup="from __main__ import find_median, array",
        number=1000))
# нахождение медианы по отсортированному массиву рвет в клочья мой алгоритм поиска медианы, хотя мой алгоритм и рабочий
# но он в 100 раз медленее
# median_sort 0.0034864000000000006
# find_median 0.3
