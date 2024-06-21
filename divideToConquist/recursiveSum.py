def recursive_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst.pop(0) + recursive_sum(lst)


ls = [1, 2, 3, 4, 5, 1, 2]

print(recursive_sum(ls))