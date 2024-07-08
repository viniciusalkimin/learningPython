def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lowers = [i for i in array[1:] if i <= pivot]
        uppers = [i for i in array[1:] if i > pivot]
        return quick_sort(lowers) + [pivot] + quick_sort(uppers)


arr = [7, 9, 3, 2, 4]
print(quick_sort(arr))
