def major_func(array, num):
    majors = []
    for i in range(1, len(array)):
        if array[i] > num:
            majors.append(array[i])
    return majors


def minor_func(array, num):
    minors = []
    for i in range(1, len(array)):
        if array[i] < num:
            minors.append(array[i])
    return minors


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    minors = minor_func(array, pivot)
    majors = major_func(array, pivot)
    return quick_sort(minors) + [pivot] + quick_sort(majors)


arr = [7, 9, 3, 2, 4]
print(quick_sort(arr))
