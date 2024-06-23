def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst.pop(0) + recursive_sum(lst)


def recursive_item_sum(lst):
    if len(lst) == 0:
        return 0
    return 1 + recursive_item_sum(lst[1:])


ls1 = [2, 4, 6]
ls2 = [1, 2, 3, 4, 5]
print(recursive_sum(ls1))
print(recursive_item_sum(ls2))
