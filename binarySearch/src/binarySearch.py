def binarySearch(ls, number: int):
    first: int = 0
    last: int = len(ls) - 1
    while first <= last:
        mid: int = (first + last) // 2
        shoot = ls[mid]
        if shoot == number:
            return mid
        if mid > number:
            last = mid - 1
        else:
            first = mid + 1
    return None


myList = []
num = 0
while len(myList) <= 1024:
    myList.append(num)
    num += 1

print(binarySearch(myList, 4))
