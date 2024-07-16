def major_func(arr, num):
    majors = []
    for i in range(1, len(arr)):
        if arr[i] > num:
            majors.append(arr[i])
    return majors


def minor_func(arr, num):
    minors = []
    for i in range(1, len(arr)):
        if arr[i] < num:
            minors.append(arr[i])
    return minors


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    minors = minor_func(arr, pivot)
    majors = major_func(arr, pivot)
    return quick_sort(minors) + [pivot] + quick_sort(majors)


a = [5, 4, 2, 1, 7, 8]
print(quick_sort(a))
