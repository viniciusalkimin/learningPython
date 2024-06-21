def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst.pop(0) + recursive_sum(lst)


ls = [2, 4, 6]

print(recursive_sum(ls))
