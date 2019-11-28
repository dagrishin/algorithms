def binary_search(mylist, number, start, stop):
    if start > stop:
        return False
    mid = (start + stop) // 2
    if number == mylist[mid]:
        return mid
    elif number > mylist[mid]:
        return binary_search(mylist, number, mid + 1, stop)
    else:
        return binary_search(mylist, number, start, mid - 1)


my_list = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
number = 83
start = 0
stop = len(my_list) - 1
print(binary_search(my_list, number, start, stop))
