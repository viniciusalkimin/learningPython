def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst.pop(0) + recursive_sum(lst)


def recursive_item_sum(lst):
    if len(lst) == 0:
        return 0
    return 1 + recursive_item_sum(lst[1:])


def recursive_biggest_item(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = recursive_biggest_item(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


ls1 = [2, 4, 6]
ls2 = [1, 2, 3, 4, 5]
ls3 = [8, 7, 10, 6, 9, 1, 3]
print(recursive_sum(ls1))
print(recursive_item_sum(ls2))
print(recursive_biggest_item(ls3))
